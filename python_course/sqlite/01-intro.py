import sqlite3

with sqlite3.connect('./python_course/sqlite/app.db') as con:
    print("Connected")