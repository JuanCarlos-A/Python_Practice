class MiPerro:
    patas = 4 #Atributo de clase
    def __init__(self, nombre :str, edad :float) -> None:
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado un perro con el nombre {nombre}')
              
    def habla(self) -> None:
        print(f"{self.nombre} dice: Guau!")

mi_perro = MiPerro("Felipe", 1)
MiPerro.patas = 3
print(mi_perro.patas)
mi_perro.patas = 5
print(mi_perro.patas)
mi_perro2 = MiPerro("John", 5)
print(mi_perro2.patas)
mi_perro.habla()