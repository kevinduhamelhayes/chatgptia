def es_palindromo(palabra):
    """Devuelve True si la palabra es palíndromo, False si no lo es"""
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo(palabra)
    if es_palindromo(palabra) == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
if __name__ == "__main__":
    run()
    