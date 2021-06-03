import sqlite3

def sql_connection():
    con = sqlite3.connect('settings.db')
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS settings(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        URL TEXT,
        API TEXT,
        language TEXT
    )""")

    cursor.execute("SELECT * FROM settings")
    if cursor.fetchone() == None:
        cursor.execute("INSERT INTO settings VALUES(?, ?, ?, ?)", (None ,"https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", "", "ru"))
        con.commit()
        #print("Connection complete!")

    return con


def get_settings(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM settings")
    data = cursor.fetchone()
    settings = {
        'id' : data[0],
        'URL' : data[1],
        'API' : data[2],
        'language' : data[3]
    }
    return settings


def update_settings(con, settings:dict):
    cursor = con.cursor()
    for key, value in settings.items():
        cursor.execute(f"UPDATE settings SET '{key}' = ? WHERE id = ?", (value, 1))
    
    con.commit()
    

def default_settings(con):
    settings = {
        'URL' : "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address",
        'API' : "",
        'language' : "ru"
    }
    update_settings(con, settings)


con = sql_connection()

