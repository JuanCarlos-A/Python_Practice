#Tarea:

#Averiguar _atributo __metodo, static method, getters y setters inheritances, circular importation

class User:
    def __init__(self, id:int, name:str, active:bool) -> None:
        self._id = id # Esto solo es una convencion para indicar que es un atributo protegido
        self.__name = name #Atributo privado __name indica que no se puede acceder desde fuera de la clase o conocido como name mangling
        self.__active = active

    def get_name(self):
        return self.__name
    

    @staticmethod
    def log() -> None:
        print('Usuario logeado')

    def log_id(self) -> None:
        print(f'Id: {self._id}')

    @staticmethod
    def mask(id, name):
        return f'x{id}x{name}x'

    def sent_credentials(self):
        id = self._id
        name = self.__name

        hashed = self.mask(id, name)

    def __private(self):
        pass

usuario = User(1, 'Juan', True)

# User.otra_funcion()

# usuario.otra_funcion()

print(usuario.get_name())

print(usuario._User__name)

print(usuario._User__private)






# print(usuario)

# print(usuario.get_name())

# print(usuario._id) #Error

# User.imprimir_mensaje()

# User.imprimir_despedida()

