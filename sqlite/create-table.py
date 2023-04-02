import sqlite3

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()
con.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100), apellido VARCHAR(100), email VARCHAR(100), password VARCHAR(100))")
con.commit()
con.close()
