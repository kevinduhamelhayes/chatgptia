def suma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

c=(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(c)
print(c+(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)*2))