import sqlite3

def sql_connection():
    con = sqlite3.connect('settings.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS settings(
        URL TEXT,
        API TEXT,
        language TEXT
    )""")

    cursor.execute("SELECT * FROM settings")
    if cursor.fetchone() == None:
        cursor.execute("INSERT INTO settings VALUES(?, ?, ?)", ("https://cleaner.dadata.ru/api/v1/clean/addres", "", "ru"))
        con.commit()
        print("Connection complete!")
    else:
        cursor.execute("SELECT * FROM settings")
        print("Everything is OK!")
        print(cursor.fetchone())
    return con



con = sql_connection()

