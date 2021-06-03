import os
from db import con, get_settings, update_settings

main_menu = (
    ("Сделать запрос", lambda: menu(trash)),
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

def show_settings():
    os.system('cls')
    settings = get_settings(con)
    for key in settings:
        print(f"{key} : {settings[key]}")  

    os.system("pause")


def change_settings(name:str):
    os.system('cls')
    settings = get_settings(con)
    value = input("Введите значение: ")
    try:
        for key in settings:
            if key == name:
                settings[key] = value
        update_settings(con, settings)
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


        


        


