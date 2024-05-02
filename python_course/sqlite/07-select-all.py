import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios;
        """,
        )
    usuario = cursor.fetchall() # Retorna una lista con tuplas de todos los registros
    print(usuario)
    print(f"Usuario 1: {usuario[0]}")