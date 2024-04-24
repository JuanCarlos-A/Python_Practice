from io import open

# Escritura con W

# text = "Hola Mundo Programador"

# archivo = open("python_course/archivos/hola-mundo.txt", "w")
# try:
#     archivo.write(text)
# except Exception as e:
#     print(f"An error ocurred : {e}")
# finally:
#     archivo.close()


# Lectura con R

# archivo = open("python_course/archivos/hola-mundo.txt", "r")

# try:    
#     text = archivo.read()
# except Exception as e:
#     print(f'An error ocurred : {e}')
# else:
#     print(text)
# finally:
#     archivo.close()


# Lectura como List

# archivo = open("python_course/archivos/hola-mundo.txt", "r")

# try:    
#     text = archivo.readlines()
# except Exception as e:
#     print(f'An error ocurred : {e}')
# else:
#     print(text)
# finally:
#     archivo.close()

## Haciendo uso del context manager y el with statement

# with open("python_course/archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines()) # Devuelve una lista con el contenido del archivo

#     archivo.seek(0) #Asignamos el puntero al primer caracter no a una linea en especifico

#     for linea in archivo:
#         print(linea)

## Prueba sin el uso de with para el iterador

# archivo = open("python_course/archivos/hola-mundo.txt", "r")

# print(archivo.readlines()) # Devuelve una lista con el contenido del archivo
    

# for linea in archivo:
#     print(linea)


##Agregar

# archivo = open("python_course/archivos/hola-mundo.txt", "a+")

# archivo.write( "\n" + str([x for x in range(1, 11)]))

# archivo.close()

## Lectura y Escritura Simultaneamente

with open("python_course/archivos/hola-mundo.txt", "r+") as archivo: # Reemplazar segun lo que le indiquemos
    texto = archivo.readlines()

    archivo.seek(0)

    texto[0] = "Programador Feliz"

    archivo.writelines(texto)