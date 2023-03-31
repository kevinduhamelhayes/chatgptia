#eliminar espacio en blanco
from pprint import pprint
string = " hola mundo "

def remove_spaces(string):
    return [char for char in string if char != " "]
sinespacios=remove_spaces(string)
print(sinespacios)

#pprint imprime de forma mas legible el diccionario
def cuenta_caracteres(string):
    return {char: string.count(char) for char in string}
pprint(cuenta_caracteres(string), width=1)

def ordena_caracteres(cuenta_caracteres):
    return sorted(cuenta_caracteres.items(), key=lambda x: x[1], reverse=True)
print(ordena_caracteres(cuenta_caracteres(string)))

def mayor_frecuencia(ordena_caracteres):
    return ordena_caracteres[0][1]
    respuesta = {}
    for key, value in ordena_caracteres.items():
        if value == mayor_frecuencia:
            respuesta[key] = value
    return respuesta
print(mayor_frecuencia(ordena_caracteres(cuenta_caracteres(string))))

def los_mas_frecuentes(ordena_caracteres):
    return [key for key, value in ordena_caracteres.items() if value == mayor_frecuencia(ordena_caracteres)]
print(los_mas_frecuentes(ordena_caracteres(cuenta_caracteres(string))))