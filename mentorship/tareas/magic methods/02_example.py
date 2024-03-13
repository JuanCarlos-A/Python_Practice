class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # Método para representar el objeto como string
        return f"Persona: {self.nombre}, Edad: {self.edad}"

    def __eq__(self, other): # Método para comparar si dos objetos son iguales
        return self.nombre == other.nombre and self.edad == other.edad

    def __lt__(self, other): # Método para comparar si un objeto es menor que otro
        return self.edad < other.edad

    def __len__(self): # Método para obtener la longitud del objeto
        return self.nombre

p1 = Persona("Juan", 25)
p2 = Persona("Maria", 30)

print(p1)  # Salida: Persona: Juan, Edad: 25
print(p1 == p2)  # Salida: False
print(p1 < p2)  # Salida: True
print(len(p1)) # Salida: 4