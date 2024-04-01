class Animal:
    def comer(self) -> None:
        print("Comiendo")

class Perro:
    def pasear(self) -> None:
        print("Paseando")

class Chanchito(Perro, Animal):
    def programar(self) -> None:
        print("Programando")

chanchito = Chanchito()

