class MiPerro:
    def __init__(self, nombre :str, edad :float) -> None:
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado un perro con el nombre {nombre}')
              
    def habla(self) -> None:
        print(f"{self.nombre} dice: Guau!")

mi_perro = MiPerro("Felipe")

mi_perro.habla()

# mi_perro2 = MiPerro("Firulais")

# print(mi_perro2.nombre)