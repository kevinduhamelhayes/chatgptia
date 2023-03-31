import random
import sys

#cadena = []
# i=0
# for i in range(1, 101):
#     if i == cadena:
#         print("Encontrado")
#         sys.exit(0)
# numero = random.randint(1, 100)
# for numero in range(101):
#     cadena.append(numero)
#     print(cadena)
#     print(numero)
#     print("No encontrado")
#     sys.exit(0)

buscar = int(input("Ingrese un numero: "))
for numero in range(1, 50):
    if numero == buscar:
        print("Encontrado")
        break
else:
        print("No encontrado")
        
for char in "Hola":
    print(char)