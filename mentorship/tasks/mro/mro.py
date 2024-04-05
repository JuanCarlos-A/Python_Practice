class PrimeraClase:
    def funcion(self):
        print("Metodo de la clase PrimeraClase")

class SegundaClase:
    def funcion(self):
        print("Metodo de la clase SegundaClase")
    
class TerceraClase(SegundaClase, PrimeraClase):
    pass

class CuartaClase(SegundaClase, TerceraClase):
    pass

# orden de ejecucion [4, 2, 3, 2, 1]

cuarto_objeto = CuartaClase()

cuarto_objeto.funcion()