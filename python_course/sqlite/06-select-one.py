import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute(
        """
        SELECT * FROM usuarios;
        """,
        )
    usuario = cursor.fetchone() # Retorna una tupla de solo un registro
    print(usuario)
    print(f"Nombre: {usuario[1]}")