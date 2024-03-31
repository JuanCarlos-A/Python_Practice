class MiPerro:

    patas = 4 #Atributo de clase

    def __init__(self, nombre :str, edad :float) -> None:
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado un perro con el nombre {nombre}')
              
    def habla(self) -> None:
        print(f"{self.nombre} dice: Guau!")

    @classmethod
    def cambiar_patas(cls, patas :int) -> None:
        cls.patas = patas
    
    @classmethod
    def sonido(cls) -> None:
        print("Guau!")

    @classmethod
    def crear_perro(cls, nombre :str, edad :float) -> "MiPerro": #Este método es un constructor alternativo
        return cls(nombre, edad) #Se crea una instancia de la clase MiPerro

mi_perro = MiPerro("Felipe", 1)
print(mi_perro.patas)
MiPerro.cambiar_patas(3)
print(mi_perro.patas)
MiPerro.sonido()

mi_perro2 = MiPerro.crear_perro("John", 5)

