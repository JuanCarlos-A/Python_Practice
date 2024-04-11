from pathlib import Path

path = Path("rutas")

# path.exists() # Verificar si el directorio existe
# path.mkdir() # Crear un directorio
# path.rmdir() # Eliminar un directorio
# path.rename("nuevo_directorio") # Renombrar un directorio

for p in path.iterdir(): # Iterar sobre los elementos de un directorio
    print(p)