class Perro:
    def __init__(self, nombre, edad, raza=None, dueño=None):
        self.nombre = self.validar_nombre(nombre)
        self.edad = self.validar_edad(edad)
        self.raza = raza
        self.dueño = dueño

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

    def pasear(self, distancia):
        print(f"{self.nombre} está caminando {distancia} km.")
        
    def saludar(self):
        if self.dueño is None:
            print(f"{self.nombre} mueve la cola, pero no tiene dueño.")
        else:
            print(f"{self.nombre} saluda a {self.dueño}.")

    def envejecer(self, años=1):
        self.edad += años
        if self.edad > 20:
            print(f"{self.nombre} ha fallecido, ya que ha alcanzado la edad máxima.")
            self.edad = 20
        
    def __str__(self):
        return f"Perro(nombre='{self.nombre}', edad={self.edad}, raza='{self.raza}', dueño='{self.dueño}')"
print(dir(Perro))
