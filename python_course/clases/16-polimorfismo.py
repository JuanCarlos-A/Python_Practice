from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando en bases de datos")

class Session(Model):
    def guardar(self):
        print("Guardando en un archivo")

def guardar(*entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()

sesion = Session()

guardar(usuario, sesion)