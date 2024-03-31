class Perro:
    def __init__(self, nombre :str, edad :float) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'Clase Perro: \nNombre: {self.nombre}\nEdad: {self.nombre}'
    
    def __del__(self) -> None:
        print(f"Chao Perro {self.nombre}")
    
    @property
    def nombre(self) -> str:
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, nombre :str) -> None:
        if nombre.strip():
            self.__nombre = nombre

my_dog = Perro("Firulais", 3)

del my_dog
