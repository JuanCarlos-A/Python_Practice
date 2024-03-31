class Perro:
    def __init__(self, nombre :str) -> None:
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        print("Pasando por getter")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre :str) -> None:
        print("Pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("John")

print(perro.nombre)