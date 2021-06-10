import os
from utils import get_addresses, get_coordinates
from db import con, get_settings, update_settings, default_settings
from request import get_response

main_menu = (
    ("Сделать запрос", lambda: request_menu()),
    ("Настройки", lambda: menu(settings)),
    ("Выход", 0)
)

settings = (
    ("Показать текущие настройки", lambda: show_settings()),
    ("Изменить URL", lambda: change_settings("URL")),
    ("Изменить API", lambda: change_settings("API")),
    ("Изменить язык", lambda: menu(language)),
    ("Вернуть настройки по-умолчанию", lambda: default_settings(con)),
    ("Назад", 0)
)

language = (
    ("Русский", lambda: change_settings("language", "ru")),
    ("Английский", lambda: change_settings("language", "en")),
    ("Назад", 0) 
)


def coordinates_menu(address:str):
    settings = get_settings(con)
    response = get_response(settings, dict(query=address, count=1))
    response = get_coordinates(response)
    print(f"Выбранный адрес находится на следующих координатах: {response[0]} , {response[1]}")
    


def request_menu():
    os.system("cls")
    address = input("Введите запрос: ")
    settings = get_settings(con)
    response = get_response(settings, dict(query=address))

    addresses = get_addresses(response)
    
    address_menu = tuple()

    for item in addresses:
        address_menu += ((item, lambda x: coordinates_menu(x)),)

    menu(address_menu)

    os.system("pause")


def show_settings():
    os.system('cls')
    settings = get_settings(con)
    for key in settings:
        print(f"{key} : {settings[key]}")  

    os.system("pause")


def change_settings(key:str, value=None):
    os.system('cls')

    if value is None:
        value = input("Введите значение: ")
    try:
        update_settings(con, dict.fromkeys([key], value))
        os.system("cls")
        print("Изменения были успешно внесены!")
        os.system("pause")
    except:
        print("Что-то пошло не так...")
        os.system("pause")


def menu(menu:tuple):
    show = True
    while show:
        os.system('cls')
        
        for i, item in enumerate(menu):
            print(f"{i+1}. {item[0]}")

        try:
            answer = int(input("Выберите пункт меню: "))
            
            if answer > 0:
                if menu[answer - 1][1] != 0:
                    try:
                        menu[answer - 1][1]()
                    except TypeError:
                        menu[answer - 1][1](menu[answer-1][0])
                        show = False
                else:
                    show = False
            else:
                raise Exception("Какая-то беда")
        except Exception as e: 
            print("Что-то пошло не так...")
            print(type(e))
            print(e)
            os.system("pause")


        


        


