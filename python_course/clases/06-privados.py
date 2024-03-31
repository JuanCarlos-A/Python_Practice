class MiPerro:

    patas = 4 #Atributo de clase

    def __init__(self, nombre :str, edad :float) -> None:
        self.__nombre = nombre
        self.edad = edad
        print(f'Se ha creado un perro con el nombre {self.__nombre}')
              
    def habla(self) -> None:
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def cambiar_patas(cls, patas :int) -> None:
        cls.patas = patas
    
    @classmethod
    def sonido(cls) -> None:
        print("Guau!")

    @classmethod
    def crear_perro(cls, nombre :str, edad :float) -> "MiPerro": #Este método es un constructor alternativo
        return cls(nombre, edad) #Se crea una instancia de la clase MiPerro
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre :str) -> None:
        self.__nombre = nombre
    

perro1 = MiPerro.crear_perro("Firulais", 5)

perro1.habla() 

print(perro1._MiPerro__nombre) #Se puede acceder al atributo __nombre

# perro1._MiPerro__nombre = "Firulaisito" #No se puede modificar el atributo __nombre

print(perro1.__dict__) # Imprime un diccionario con las propiedades de la clase.
