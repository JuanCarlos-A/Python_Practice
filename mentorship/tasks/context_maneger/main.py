# Memory Leak del Context Maneger

# Añadido en el PEP 343

# Ejemplo 1

try: 
    file = open("Mentorship/tasks/context_maneger/example.txt", "w")
    file.write("Hello World!")
finally:
    file.close()

with open("Mentorship/tasks/context_maneger/example.txt", "w") as file:
    file.write("Hello World!")


# Ejemplo 2

class ContextManager:
    def __enter__(self):
        print("Entrando al Context Manager")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Salida del Context Manager")
        return True
    
with ContextManager() as manager:
    print("Dentro del Context Manager")
    print(manager)


## Ejemplo 3

# file = open("Mentorship/tasks/context_maneger/example.txt", "w")

# try:
#     file.write("Hello World!")

# except Exception as e: 
#     print(f'An error ocurred {e}')

# finally:
# # Nos aseguramos de cerrar el recuros despues de la ejecucion asi ocurra un error
#     file.close()

# Ejemplo 4

# expresion = open("Mentorship/tasks/context_maneger/example.txt", "w")

# enter = type(expresion).__enter__

# exit = type(expresion).__exit__