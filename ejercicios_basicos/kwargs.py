def get_product(**datos):
    print(datos["id"], datos["nombre"], datos["precio"])

get_product(id=1, nombre="camisa", precio=100)
get_product(id=2, nombre="pantalon", precio=200)