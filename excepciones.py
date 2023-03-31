#capturables
try:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese un numero: "))
except ValueError:
    print("Error, debe ingresar un numero")
except NameError:
    print("ocurrio un error de nombre")
else:
    print("No hubo error")
finally:
    print("se ejecutara siempre")