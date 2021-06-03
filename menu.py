import os
from db import con, get_settings, update_settings
from request import send_request

main_menu = (
    ("Сделать запрос", lambda: request_menu()),
    ("Настройки", lambda: menu(settings)),
    ("Выход", 0)
)

settings = (
    ("Показать текущие настройки", lambda: show_settings()),
    ("Изменить URL", lambda: change_settings("URL")),
    ("Изменить API", lambda: change_settings("API")),
    ("Изменить язык", lambda: change_settings("language")),
    ("Назад", 0)
)

trash = (
    ("Послать всё", 0),
    ("Назад", 0) 
)

def request_menu():
    os.system("cls")
    query = input("Введите запрос: ")
    settings = get_settings(con)
    response = send_request(settings, query)
    
    for item in response:
        print(item)

    os.system("pause")

def show_settings():
    os.system('cls')
    settings = get_settings(con)
    for key in settings:
        print(f"{key} : {settings[key]}")  

    os.system("pause")


def change_settings(key:str):
    os.system('cls')

    value = input("Введите значение: ")
    try:
        update_settings(con, dict.fromkeys([key], value))
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
                    menu[answer - 1][1]()
                else:
                    show = False
            else:
                raise Exception("Некорректный ввод")
        except: 
            print("Некорректный ввод")
            os.system("pause")


        


        


