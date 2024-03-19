""" Docstring for Module """

import dataclasses

CHANCHITO = "feliz" #Representacion de una constante en mayusculas
A = 12
B = 13

#Decorador para que automaticamente se generen los metodos de una clase, ejemplo Contructor __init
@dataclasses.dataclass
class Example:
    """ Class representing a example"""
    a: int
    b: int

    def execute(self):
        """ Method to execute a sum"""
        print(self.a + self.b)
