import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    con.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100), apellido VARCHAR(100), email VARCHAR(100), password VARCHAR(100))")
  