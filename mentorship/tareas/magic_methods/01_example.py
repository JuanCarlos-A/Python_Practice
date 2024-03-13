class Rectabgulo:
    #Metodo Constructor que recibe como primer parametro self, especiica usar el atributo del objeto
    def __init__(self, height:float, width:float):
        self.height = height
        self.width = width
    
    # Método para representar el objeto como string
    def __str__(self) -> str:
        return f'Rectangle({self.height}, {self.width})'
    
    def __eq__(self, object: object) -> bool: # Método para comparar si dos objetos son iguales
        return self.height == object.height and self.width == object.width