class Persona:
    """Clase que representa a una persona con sus atributos nombre y apellido"""
    def __init__(self, nombre, apellido):
        """Constructor de la clase"""
        self.__nombre = nombre
        self.__apellido = apellido

    @property # Decorador que indica que el método es un getter
    def nombre(self):
        """Método getter del atributo nombre"""
        return self.__nombre

    @nombre.setter  # Decorador que indica que el método es un setter
    def nombre(self, nombre):
        """Método setter del atributo nombre"""
        self.__nombre = nombre

    def get_apellido(self):
        """Método getter del atributo apellido"""
        return self.__apellido
    
    def set_apellido(self, apellido):
        """Método setter del atributo apellido"""
        self.__apellido = apellido

persona = Persona('Juan', 'Perez')
print(persona.nombre)
persona.nombre = 'Karla'
print(persona.nombre)

print(persona.get_apellido())
persona.set_apellido('Lara')
print(persona.get_apellido())
