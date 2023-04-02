import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        ("Maria", "Gomez","mariagomez@gmail.cp,","123456"),
        ("javiera", "Gomez","javieragomez@gmail.com","123456"),
        ("jasviera", "ssGomez","jssvieragomez@gmail.com","123456")
    ]
    cursor.executemany("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)", usuarios)

