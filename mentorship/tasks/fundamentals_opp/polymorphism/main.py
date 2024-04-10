class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Guau"
    
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Miau"

def sonido_animal(animal):
    print(animal.sonido())

perro = Perro("Firulais")
gato = Gato("Garfield")

sonido_animal(perro)
sonido_animal(gato)


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


p = Persona("Juan")

print(p.__dict__) # {'nombre': 'Juan'}