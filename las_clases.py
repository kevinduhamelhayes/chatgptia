mensaje = "Hola mundo"

#clases son planos de construccion para poder crear objetos
#objetos son instancias de una clase
class Perro:
    #dentro de una clase se definen atributos y metodos(funciones)
    #atributos son variables
    #metodos son funciones
    #self es una referencia al objeto que se esta creando
    #self.nombre es una variable de instancia
    #nombre es una variable de clase
    #__init__ es el constructor de la clase
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        print("guau guau")
    def __str__(self):
        return f"Perro {self.nombre}, edad: {self.edad}"
mi_perro = Perro("firulais", 5)
mi_perro2 = Perro("firulais2", 6)

print(mi_perro)
print(mi_perro2)
print(mi_perro.patas)
print(mi_perro2.patas)
print(Perro.patas)
mi_perro.ladrar()