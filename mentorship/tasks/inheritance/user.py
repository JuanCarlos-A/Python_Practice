#Tarea:

#Averiguar _atributo __metodo, static method, getters y setters inheritances, circular importation

class User:
    def __init__(self, id:int, name:str, active:bool) -> None:
        self._id = id # Esto solo es una convencion para indicar que es un atributo protegido
        self.__name = name #Atributo privado __name indica que no se puede acceder desde fuera de la clase o conocido como name mangling
        self.__active = active

    def __str__(self) -> str:
        return f'User:\nNombre: {self.__name}\nActivo: {self.__active}'
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name:str) -> None:
        self.__name = name

    @staticmethod #Metodo estatico
    def imprimir_mensaje() -> None:
        print('Hola mundo')
    
    def imprimir_despedida() -> None:
        print('Adios mundo')
    
    imprimir_despedida = staticmethod(imprimir_despedida) #Tambien podemos crear un metodo estatico de esta forma
    

usuario = User(1, 'Juan', True)

print(usuario)

print(usuario.get_name())

print(usuario._id) #Error

User.imprimir_mensaje()

User.imprimir_despedida()

