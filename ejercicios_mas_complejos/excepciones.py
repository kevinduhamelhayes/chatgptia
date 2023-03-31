#capturables
# try:
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese un numero: "))
# except ValueError:
#     print("Error, debe ingresar un numero")
# except NameError:
#     print("ocurrio un error de nombre")
# else:
#     print("No hubo error")
# finally:
#     print("se ejecutara siempre")

def dividir(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("Los valores deben ser numericos")
    except:
        print("Ocurrio un error")
    else:
        print("No hubo error")
    finally:
        print("Se ejecutara siempre")