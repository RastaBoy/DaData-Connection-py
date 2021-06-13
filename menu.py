import os
from typing import Iterable
from utils import get_addresses, get_coordinates, dict_formater, printer
from db import con, get_settings, update_settings, default_settings
from request import get_response




def dialogue_form(text):
    return {
        'description' : text,
        'menu_items' : [
            ("Да", lambda: True),
            ("Нет", lambda: False)
        ] 
    }

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
        address_menu = dict()
        address_menu['description'] = "Список адресов, подходящих под Ваш запрос:"
        address_menu['menu_items'] = []

        for item in addresses:
            #address_menu['menu_items'].append((item, lambda x: print(f"Выбранный адрес находится на следующих координатах: {','.join(coordinates_menu(x))}"), item))
            address_menu['menu_items'].append((item, lambda x: printer(f"Выбранный Вами адрес - {x}\nНаходится на следующих координатах: {','.join(coordinates_menu(x))}", result=0), item))

        address_menu['menu_items'].append(("Назад", lambda: 0))
        menu(address_menu)
    else: 
        printer("К сожалению, таких адресов не найдено...")



def show_settings():
    os.system('cls')
    settings = get_settings(con)
    printer(dict_formater(settings))



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


def set_language(lang:str):
    result = menu(dialogue_form("Вы уверены, что хотите изменить язык?"))
    if result == True:
        change_settings('language', lang)
        printer('Язык был изменен!')
    return 0


main_menu = {
    'description' : "--- DaData Connection Py ---",
    'menu_items' : [
        ("Сделать запрос", lambda: request_menu()),
        ("Настройки", lambda: menu(settings)),
        ("Выход", lambda: 0)
    ]
}

settings = {
    'description' : "--- Меню пользовательских настроек ---",
    'menu_items' : [
        ("Показать текущие настройки", show_settings),
        ("Изменить URL", lambda: change_settings("URL") if menu(dialogue_form('Вы уверены, что хотите изменить URL?')) else None),
        ("Изменить API", lambda: change_settings("API") if menu(dialogue_form('Вы уверены, что хотите изменить API?')) else None),
        ("Изменить язык", lambda: menu(language)),
        ("Вернуть настройки по-умолчанию", lambda: default_settings(con) if menu(dialogue_form('Вы уверены, что хотите вернуть настройки по-умолчанию?')) else None),
        ("Назад", lambda: 0)
    ]
}

language = {
    'description' : "--- Меню выбора языка ---",
    'menu_items' : [
        ("Русский", set_language, 'ru'),
        ("Английский", set_language, 'en'),
        ("Назад", lambda: 0) 
    ]
}




def menu(menu:dict):

    # if res == None -> continue
    # if res == 0 -> break
    # else -> res 

    while True:
        os.system('cls')
        
        print(menu['description'])
        for i, item in enumerate(menu['menu_items']):
            print(f"{i+1}. {item[0]}")

        try:
            answer = int(input("Выберите пункт меню: "))
            
            if answer > 0:
                item = menu['menu_items'][answer-1]
                result = item[1](*item[2:])
                if result is None:
                    continue
                elif result == 0:
                    break
                else:
                    return result
            else:
                raise Exception("Некорректный ввод! Попробуйте еще раз...")
        except Exception as e: 
            print("Что-то пошло не так...")
            print(type(e))
            print(e)
            os.system("pause")



        


        

