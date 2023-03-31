# numero= 1
# while numero < 2000:
#     print(numero)
#     numero *= 2
# # Compare this snippet from while.py:

# comando = ""

# while comando.lower() != "salir":
#     comando = input(">")
#     print("Ejecutando comando " + comando)
    
while True:
    comando = input(">")
    print("Ejecutando comando " + comando)
    if comando.lower() == "salir":
        break