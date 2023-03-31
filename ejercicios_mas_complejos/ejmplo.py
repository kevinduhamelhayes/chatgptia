from abc import ABC, abstractmethod
class Modelo(ABC):
    tabla = None
    def __init__(self):
        if not self.tabla:
            print("No hay datos para mostrar.")
    def guardar(self):
        print(f"guardando datos en la tabla {self.tabla}")
        
    def buscar_por_id(self, id):
        print(f"buscando datos en la tabla {self.tabla} con id {id}")
        
        
class Usuario(Modelo):
    tabla = "usuarios"
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        
    def __str__(self):
        return f"Usuario(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}', password='{self.password}')"



model=Usuario("Juan", "Perez", "", "123456")
print(model)