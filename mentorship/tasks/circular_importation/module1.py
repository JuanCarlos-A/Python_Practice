import module2

def example():
    module2.another_example()

#La importacion de module2 en module1 y viceversa genera un error de circular importation
#Para solucionar esto se puede importar el modulo en el metodo que se requiera