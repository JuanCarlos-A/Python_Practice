class Rectabgulo():
    #Metodo Constructor que recibe como primer parametro self
    def __init__(self, height:float, width:float):
        self.height = height
        self.width = width
    
    #Esto es un ejemplo de lo que el PEP 484 sugiere
    def __str__(self) -> str:
        return f'Rectangle({self.height}, {self.width})'
    
    def __eq__(self, __value: object) -> bool:
        pass