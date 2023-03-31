#calculadora
import math
import sys
print("Bienvenido a la calculadora")
print("para salir escriba salir")
print("las operaciones disponibles son: suma, resta, multiplicacion, division, potencia, raiz")
resultado = ""
while True:
    if not resultado: 
        resultado = input("ingrese el primer numero: ")
        if resultado.lower() == "salir":
           break
        resultado = int(resultado)
    op = input("ingrese la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese el segundo numero: ")
    n2= int(n2)
    if op.lower() == "+":
        resultado += n2
    elif op.lower() == "-":
        resultado -= n2
    elif op.lower() == "*":
        resultado *= n2
    elif op.lower() == "/":
        resultado /= n2
    elif op.lower() == "**":
        resultado **= n2
    elif op.lower() == "//":
        resultado = math.sqrt(resultado) 
    else:
        print("operacion invalida")
    print("el resultado es: " + str(resultado))
    resultado= ""
    
        
        