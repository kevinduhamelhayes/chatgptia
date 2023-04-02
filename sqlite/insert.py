import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)", ("Juan", "Perez", "juanperez@gmail.com", "123456"))
    cursor.execute("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)", ("Maria", "Gomez","mariagomez@gmail.cp,","123456"))