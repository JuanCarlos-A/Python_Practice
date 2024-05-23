import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        " INSERT INTO usuarios VALUES (?, ?);",
        (1, "Hola Mundo"),
        )
    print("Record inserted")