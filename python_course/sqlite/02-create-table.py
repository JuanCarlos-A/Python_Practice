import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY, nombre VARCHAR(50));
        """
        )
    print("Table created")
    con.commit()

