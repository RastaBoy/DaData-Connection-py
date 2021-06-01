import os

main_menu = {
    '1' : ("Сделать запрос", lambda: menu(trash)),
    '2' : ("Настройки", lambda: menu(settings)),
    '3' : ("Выход", 0)
}

settings = {
    '1' : ("Ввести никнейм", 0),
    '2' : ("Назад", 0)
}

trash = {
    '1' : ("Послать всё нахуй", 0),
    '2' : ("Назад", 0) 
}


def menu(menu:dict):
    show = True
    while show:
        os.system('cls')
        
        for i in menu:
            print(f'{i}. {menu[i][0]}')

        answer = input("Выберите пункт меню: ")
        for i in menu:
            if i == answer:
                if menu[i][1] == 0:
                    show = False
                else:
                    menu[i][1]()



        


