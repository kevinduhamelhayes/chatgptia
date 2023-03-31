# Description: Ejemplo de if
# edad= int(input("Escribe tu edad: "))

# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad == 17:
#     print("Casi eres mayor de edad")
# elif edad >= 60:
#     print("Eres un adulto mayor y tienes descuento")
# else:
#     print("Eres menor de edad")
# print("Fin del programa")


# edad= int(input("Escribe tu edad: "))
# mensaje= "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
# print(mensaje)

# Description: Ejemplo de and
gas= input("¿Hay gasolina? ")
encendido= input("¿Esta encendido? ")
if gas == "si" and encendido == "si":
    print("Puedes arrancar")   