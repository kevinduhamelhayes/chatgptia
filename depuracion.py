def largo(cadena):
    longitud = 0
    for caracter in cadena:
        longitud = longitud + 1
    return longitud

largo("Hola")
print(largo("Hola"))
