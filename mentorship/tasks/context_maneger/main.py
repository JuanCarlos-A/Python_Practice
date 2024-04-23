# Memory Leak del Context Maneger

# Añadido en el PEP 343

# Ejemplo 1

# Ejemplo 2

# Ejemplo 3

file = open("example.txt", "w")

try:
    file.write("Hello World!")

except Exception as e: 
    print(f'An error ocurred {e}')

finally:
# Nos aseguramos de cerrar el recuros despues de la ejecucion asi ocurra un error
    file.close()