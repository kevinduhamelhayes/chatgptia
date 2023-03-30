import math

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    else:
        return a / b

# Función para calcular la potencia de un número
def potencia(a, b):
    return a ** b

# Función para calcular la raíz cuadrada de un número
def raiz_cuadrada(a):
    if a < 0:
        return "No se puede calcular la raíz de un número negativo"
    else:
        return a ** 0.5

# Función para calcular el logaritmo natural de un número
def logaritmo(a):
    if a <= 0:
        return "No se puede calcular el logaritmo de un número menor o igual a cero"
    else:
        return math.log(a)

# Función para imprimir el menú de opciones
def imprimir_menu():
    print("=== Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Logaritmo natural")
    print("8. Salir")

# Ciclo principal de la calculadora
while True:
    # Imprimir el menú de opciones
    imprimir_menu()

    # Pedir al usuario que seleccione una opción
    opcion = input("Selecciona una opción: ")

    # Realizar la operación correspondiente según la opción seleccionada
    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = sumar(a, b)
        print("El resultado es:", resultado)
    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = restar(a, b)
        print("El resultado es:", resultado)
    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = multiplicar(a, b)
        print("El resultado es:", resultado)
    elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = dividir(a, b)
        print("El resultado es:", resultado)
    elif opcion == "5":
        a = float(input("Ingresa el número base: "))
        b = float(input("Ingresa el exponente: "))
        resultado = potencia(a, b)
        print("El resultado es:", resultado)
    elif opcion == "6":
        a = float(input("Ingresa el número: "))
        resultado = raiz_cuadrada(a)
        print("El resultado es:", resultado)
    elif opcion == "7":
        a = float(input("Ingresa el número: "))
        resultado = logaritmo(a)
        print("El resultado es:", resultado)
    elif opcion == "8":
        print("Gracias por usar la calculadora")
        break


        
