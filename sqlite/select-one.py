import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (1,))
    usuario = cursor.fetchone()
    print(usuario)