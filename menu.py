import os
from typing import Iterable
from utils import get_addresses, get_coordinates
from db import con, get_settings, update_settings, default_settings
from request import get_response

main_menu = (
    ("Сделать запрос", lambda: request_menu()),
    ("Настройки", lambda: menu(settings)),
    ("Выход", lambda: 0)
)

settings = (
    ("Показать текущие настройки", lambda: show_settings()),
    ("Изменить URL", lambda: change_settings("URL")),
    ("Изменить API", lambda: change_settings("API")),
    ("Изменить язык", lambda: menu(language)),
    ("Вернуть настройки по-умолчанию", lambda: default_settings(con)),
    ("Назад", lambda: 0)
)

language = (
    ("Русский", lambda: change_settings("language", "ru")),
    ("Английский", lambda: change_settings("language", "en")),
    ("Назад", lambda: 0) 
)

dialogue = (
    ("Да", lambda x: x()),
    ("Нет", lambda: 0)
)

def coordinates_menu(address:str):
    settings = get_settings(con)
    response = get_response(settings, dict(query=address, count=1))
    response = get_coordinates(response)
    return response
    


def request_menu():
    os.system("cls")
    address = input("Введите запрос: ")
    settings = get_settings(con)
    response = get_response(settings, dict(query=address))

    addresses = get_addresses(response)
    
    address_menu = list()

    for item in addresses:
        address_menu.append((item, lambda x: print(f"Выбранный адрес находится на следующих координатах: {','.join(coordinates_menu(x))}"), item))

    address_menu.append(("Назад", lambda: 0))
    menu(address_menu)



def show_settings():
    os.system('cls')
    settings = get_settings(con)
    for key in settings:
        print(f"{key} : {settings[key]}")  



def change_settings(key:str, value=None):
    os.system('cls')

    if value is None:
        value = input("Введите значение: ")
    try:
        update_settings(con, dict.fromkeys([key], value))
        os.system("cls")
        print("Изменения были успешно внесены!")
    except:
        print("Что-то пошло не так...")


def menu(menu:Iterable):
    while True:
        os.system('cls')
        
        for i, item in enumerate(menu):
            print(f"{i+1}. {item[0]}")

        try:
            answer = int(input("Выберите пункт меню: "))
            
            if answer > 0:
                item = menu[answer-1]
                func = item[1]
                if func(*item[2:]) == 0:
                    break
                else:
                    os.system("pause")
            else:
                raise Exception("Некорректный ввод! Попробуйте еще раз...")
        except Exception as e: 
            print("Что-то пошло не так...")
            print(type(e))
            print(e)
            os.system("pause")



        


        


