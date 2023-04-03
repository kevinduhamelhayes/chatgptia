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
        self.__nombre = nombre
        self.edad = edad
    @property
    def get_nombre(self):
        return self.__nombre
    @get_nombre.setter
    def set_nombre(self, __nombre):
        if not isinstance(__nombre, str):
            raise ValueError("El nombre debe ser un string")
        elif len(__nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        elif len(__nombre) > 20:
            raise ValueError("El nombre debe tener menos de 20 caracteres")
        elif __nombre.isnumeric():
            raise ValueError("El nombre no puede ser numerico")
        
            self.__nombre = nombre
# mi_perro = Perro("firulais", 5)
#     def __del__(self, nombre, edad):
#         print(f"Se ha eliminado el objeto{self.nombre}")
#     @classmethod
#     def ladrar(cls):
#         print("guau guau")
#     def __str__(self):
#         return f"Perro {self.__nombre}, edad: {self.edad}"
# mi_perro = Perro("firulais", 5)
# mi_perro2 = Perro("firulais2", 6)

# print(mi_perro)
# print(mi_perro2)
# print(mi_perro.patas)
# print(mi_perro2.patas)
# print(Perro.patas)
# mi_perro.ladrar()
# del mi_perro
#metodos magicos
# __init__ constructor
# __str__ string
# __repr__ string
# __add__ suma
# __sub__ resta
# __mul__ multiplicacion
# __truediv__ division
# __floordiv__ division entera
# __mod__ modulo
# __pow__ potencia
# __eq__ igual
# __ne__ diferente
# __lt__ menor que
# __gt__ mayor que
# __le__ menor o igual que
# __ge__ mayor o igual que
# __len__ longitud
# __getitem__ indexacion
# __setitem__ asignacion
# __delitem__ eliminacion
# __iter__ iteracion
# __next__ siguiente iteracion
# __contains__ in
# __call__ llamada
# __enter__ with
# __exit__ with
# __get__ descriptor
# __set__ descriptor
# __delete__ descriptor
# __new__ constructor
# __class__ clase
