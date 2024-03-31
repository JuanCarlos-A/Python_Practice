class Animal:
    def comer(self) -> None:
        print("Comiendo")

class Perro(Animal):
    def pasear(self) -> None:
        print("Paseando")

perro = Perro()

perro.comer()

class Chanchito(Perro):
    def programar(self) -> None:
        print("Programando")

chanchito = Chanchito()

chanchito.comer()

chanchito.pasear()
