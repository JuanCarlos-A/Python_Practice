from abc import ABC, abstractmethod

class ClaseAbstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass


class Clase(ClaseAbstracta):
    def metodo(self):
        super().metodo_abstracto



#Ejemplo Usando ABC

class FiguraGeometrica(ABC):
    @abstractmethod
    def lados_figura(self):
        pass

class Triangulo(FiguraGeometrica):
    def lados_figura(self) -> str:
        return "Tengo 3 lados"
    
class Cuadrado(FiguraGeometrica):
    def lados_figura(self) -> str:
        return "Tengo 4 lados"
    
class Hexagono(FiguraGeometrica):
    def lados_figura(self) -> str:
        return "Tengo 6 lados"
    
triangle = Triangulo()
square = Cuadrado()
hexagon = Hexagono()

print(f'Triangulos : {triangle.lados_figura()}\nCuadrado : {square.lados_figura()}\nHexagono : {hexagon.lados_figura()}')


class ClaseA(ABC):
    @abstractmethod
    def imprimir(self):
        print("Hello")
    
    def saludar(self, nombre :str) -> None:
        print(f'Hello {nombre}')

class ClaseB(ClaseA):
    def imprimir(self):
        return super().saludar("John")

objeto = ClaseB()

objeto.saludar()

# # No podemos crear una instancia de una clase Abstracta con un metodo Abstracto
# objeto = ClaseA()

# objeto.imprimir()


