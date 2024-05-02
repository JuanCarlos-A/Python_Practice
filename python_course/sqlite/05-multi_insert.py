import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    cursor = con.cursor()
    datos_usuarios = [
        (2, "Chanchito Feliz"),
        (3, "Chanchisto Triste"),
    ]
    cursor.executemany(
        " INSERT INTO usuarios VALUES (?, ?);",
        datos_usuarios,
        )
    print("Record inserted")