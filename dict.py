#diccionario ejemplo
punto = {'x': 4, 'y': 5}
punto2 = dict(x=4, y=5)
print(punto)
print(punto2)
print(punto['x'])
print(punto['y'])

#añadir un elemento al diccionario
punto['z'] = 10

if 'a' in punto:
    print(punto['a'])
print(punto.get('a', 0))


#recorrer un diccionario
for key, value in punto.items():
    print(key, value)

#recorrer un diccionario de base de datos
usuarios = {
    {"id": 1, "nombre": "juan"},
    {"id": 2, "nombre": "jacinto"},
    {"id": 3, "nombre": "miguel"}}
#operador de desempaquetado
lista = [1, 2, 3]
print(*lista)
lista2 = [*range(1, 100)]
listacompleja = [*range(1, 100), *"hola"]
print(listacompleja)
#operador de desempaquetado de diccionarios
desempaquetado = {**usuarios}
print(desempaquetado)