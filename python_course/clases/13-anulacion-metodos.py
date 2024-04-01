class Ave:
    def __init__(self) -> None:
        self.volador = "Volador"

    def vuela(self):
        print("Vuela ave")

class Pato(Ave):
    def __init__(self) -> None:
        super().__init__()
        self.nada = "Nadador"

    def vuela(self):
        print("Vuela Pato")

pato = Pato()

pato.vuela()

print(pato.volador, pato.nada)
