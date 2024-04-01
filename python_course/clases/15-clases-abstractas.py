from abc import ABC, abstractmethod

class Model(ABC):
    # def __init__(self) -> None:
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")
    @abstractmethod
    def guardar(self) -> None:
        print(f'Guardando {self.tabla} en BBDD')

    @property
    @abstractmethod
    def tabla(self):
        pass
    
    @classmethod
    def buscar_por_id(self, _id :float) ->None:
        print(f'Buscando por id {_id} en la tabla {self.tabla}')

class Usuario(Model):
    tabla = "Usuario"

    def guardar(self) -> None:
        print("Guardando usuario")


usuario = Usuario()

usuario.guardar()

Usuario.buscar_por_id(155)
