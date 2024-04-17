from pathlib import Path

path = Path("python_course/rutas")

# path.exists() # Verificar si el directorio existe
# path.mkdir() # Crear un directorio
# path.rmdir() # Eliminar un directorio
# path.rename("nuevo_directorio") # Renombrar un directorio

for p in path.iterdir(): # Iterar sobre los elementos de un directorio
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]

archivos_filtrados = [p for p in path.glob("01*.py")]

archivos_filtrados = [p for p in path.glob("01*.py")]

archivos_filtrados = [p for p in path.glob("01*.py")]

archivos_filtrados = [p for p in path.rglob("**/*.py")]


print(archivos_filtrados)