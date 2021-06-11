import os
from typing import Iterable
from utils import get_addresses, get_coordinates
from db import con, get_settings, update_settings, default_settings
from request import get_response

main_menu = (
    ("--- DaData Connection Py --- \n", ),
    ("Сделать запрос", lambda: request_menu()),
    ("Настройки", lambda: menu(settings)),
    ("Выход", lambda: 0)
)

settings = (
    ("--- Меню пользовательских настроек ---\n", ),
    ("Показать текущие настройки", lambda: show_settings()),
    ("Изменить URL", lambda: change_settings("URL")),
    ("Изменить API", lambda: change_settings("API")),
    ("Изменить язык", lambda: menu(language)),
    ("Вернуть настройки по-умолчанию", lambda: default_settings(con)),
    ("Назад", lambda: 0)
)

language = (
    ("--- Меню выбора языка ---\n", ),
    ("Русский", lambda: change_settings("language", "ru")),
    ("Английский", lambda: change_settings("language", "en")),
    ("Назад", lambda: 0) 
)

dialogue = (
    ("Вы уверены?"),
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
    if len(addresses) > 0:
        address_menu = list()
        address_menu.append(("Выберите подходящий вам адрес: ", ))

        for item in addresses:
            address_menu.append((item, lambda x: print(f"Выбранный адрес находится на следующих координатах: {','.join(coordinates_menu(x))}"), item))

        address_menu.append(("Назад", lambda: 0))
        func = menu(address_menu)
        os.system("pause")
        return func
    else: 
        print("К сожалению, таких адресов не найдено...")
        return 1



def show_settings():
    os.system('cls')
    settings = get_settings(con)
    for key in settings:
        print(f"{key} : {settings[key]}")  
    return 1


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
            if i == 0:
                print(item[0])
            else:
                print(f"{i}. {item[0]}")

        try:
            answer = int(input("Выберите пункт меню: "))
            
            if answer > 0:
                item = menu[answer]
                func = item[1](*item[2:])
                if func is None:
                    return -1
                elif func == 0:
                    return -1
                elif func == 1:
                    os.system("pause")
                    pass
            else:
                raise Exception("Некорректный ввод! Попробуйте еще раз...")
        except Exception as e: 
            print("Что-то пошло не так...")
            print(type(e))
            print(e)
            os.system("pause")



        


        

