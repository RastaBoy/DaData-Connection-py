import sqlite3
from random import randint

db = sqlite3.connect('settings.db')
sql = db.cursor()



sql.execute("""CREATE TABLE IF NOT EXISTS settings(
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()
def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM settings WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO settings VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()
    else:
        print("Already has")

    for value in sql.execute("SELECT * FROM settings"):
        print(value)



