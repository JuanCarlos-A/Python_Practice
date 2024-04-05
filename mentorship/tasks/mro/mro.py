class PrimeraClase:
    pass

class SegundaClase:
    pass
    
class TerceraClase(SegundaClase, PrimeraClase):
    pass

class CuartaClase:
    def funcion(self):
        print("Metodo de la clase CuartaClase")
        

class QuintaClase:
    def funcion(self):
        print("Metodo de la clase QuintaClase")
        

class SextaClase(CuartaClase, QuintaClase):
    def funcion(self):
        print("Metodo de la clase SextaClase")
        

class SeptimaClase(TerceraClase, SextaClase):
    pass
        

# orden de ejecucion [4, 2, 3, 2, 1]

septima = SeptimaClase()

septima.funcion()
# septima.__mro__()
print(SeptimaClase.__mro__)
