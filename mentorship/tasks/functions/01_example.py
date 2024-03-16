def saludar():
    print("¡Hola, mundo!")

saludar()

class Animal:
    def __init__(self, nombre : str, raza : str):
        self.nombre = nombre
        self.raza = raza
    
    def info(self) -> str:
        a = f"Nombre: {self.nombre}, Raza: {self.raza}"
        return a
    
# ani2 = Animal("Lina")

# print(ani2.info())

ani = Animal("Luna", "Pastor Aleman")

print(ani.info()) 
    