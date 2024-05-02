# Memory Leak del Context Maneger


# Añadido en el PEP 343


# Ejemplo 1

# try: 
#     file = open("Mentorship/tasks/context_maneger/example.txt", "w")
#     file.write("Hello World!")
# finally:
#     file.close()

# with open("Mentorship/tasks/context_maneger/example.txt", "w") as file:
#     file.write("Hello World!")


# Ejemplo 2

# class ContextManager:
#     def __enter__(self):
#         print("Entrando al Context Manager")
#         return self
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print("Salida del Context Manager")
#         print(f"Tipo de excepcion: {exc_type}")
#         print(f"Valor de excepcion: {exc_value}")
#         print(f"Traceback: {exc_tb}")
    
# with ContextManager() as manager:
#     print("Dentro del Context Manager")
#     print(manager)


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

# class ExampleConstexManager:
#     def __enter__(self):
#         print("Entrando al metodo __enter__ del Context Manager Protocol")
#         return "Soy un Objeto tipo String"
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         print("Dejando el context manager")

#         if isinstance(exc_value, IndexError):
#             print("Error de Indice")
#             print(f'Tipo de Exception {exc_type}')
#             print(f'Message Exception {exc_value}')
#             print(f'Traceback {exc_tb}')
#             return True
        

# with ExampleConstexManager() as manager:
#     print(manager)
#     manager[100]


# Ejmplo 5

# class ContextManager:
#     def __init__(self, path_file) -> None:
#         self.path_file = path_file
    
#     def __enter__(self):
#         self.file = open(self.path_file, "w")
#         return self.file
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         if self.file:
#             self.file.close()


# Example 6

# from contextlib import contextmanager

# @contextmanager
# def funcion_generator():
#     try:
#         print("Entando al Context Manager")
#         file = open("Mentorship/tasks/context_maneger/example.txt", "w")
#         yield file
#     finally:
#         file.close()
#         print("Saliendo del Context Manager")