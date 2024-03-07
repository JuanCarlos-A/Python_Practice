nombre_curso = "Ultimate Python" # Cadena de caracteres. String

descripcion_curso = """
Ultimate Python

Este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programadro en Python.

"""

print(len(nombre_curso)) # 14

print(nombre_curso[0]) # U / Esto funciona porque las cadenas de caracteres son secuencias

print(nombre_curso[0:8]) # Ultimate / Como es una secuencia podemos hacer slicing

print(nombre_curso[0:7:2]) # Utmt / Slicing con saltos

print(nombre_curso[::2]) # Utmt yhn / Slicing con saltos

print(nombre_curso[::-1]) # nohtyP etamitlU / Invertir una cadena de caracteres

print(nombre_curso[9:])
