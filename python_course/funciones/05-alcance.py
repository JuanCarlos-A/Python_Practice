saludo = "Hola Global" # Variable global

def saludar():
    global saludo # Variable global
    saludo = "Hola Mundo" # Definimos esta variable como local

def saludaChanchito():
    saludo = "Hola Chanchito Feliz"


print(saludo)

saludar()

print(saludo)