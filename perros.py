class Perro:
    def __init__(self, nombre, edad):
        self.nombre = self.validar_nombre(nombre)
        self.edad = self.validar_edad(edad)

    def validar_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        return nombre.strip()

    def validar_edad(self, edad):
        if not isinstance(edad, int) or edad < 0 or edad > 20:
            raise ValueError("La edad debe ser un entero entre 0 y 20 años.")
        return edad

    def ladrido(self):
        print("¡Guau! ¡Guau!")

    def lamer(self, objeto):
        print(f"{self.nombre} está lamiendo {objeto}.")

    def __str__(self):
        return f"Perro(nombre='{self.nombre}', edad={self.edad})"
perro1 = Perro("Fido", 5)
print(perro1)
Perro(nombre='Fido', edad=5)
perro2 = Perro("Rex", 25)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in __init__
#   File "<stdin>", line 10, in validar_edad
# ValueError: La edad debe ser un entero entre 0 y 20 años.