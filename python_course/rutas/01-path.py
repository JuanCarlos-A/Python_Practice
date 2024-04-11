from pathlib import Path

path = Path("hola-mundo/mi-archivo.py")

print(
    path.name,
    path.suffix,
    path.stem,
    path.parent,
    path.absolute(),
)

p = path.with_name("chanchito_feliz.py")
print(p)

path_1 = Path("hola-mundo/mi-archivo")

pa = path_1.with_suffix(".txt")

print(pa)


# # Crear un objeto Path
# path = Path(r"python_course\rutas\01-path.py") # Windows

# # Obtener la ruta absoluta
# print(path.absolute())

# # Obtener el nombre del archivo
# print(path.name)

# # Obtener la extensión del archivo
# print(path.suffix)

# # Obtener el nombre del archivo sin la extensión
# print(path.stem)

# # Obtener el directorio padre
# print(path.parent)

# # Obtener el directorio padre del directorio padre
# print(path.parent.parent)

# # Obtener el directorio padre del directorio padre del directorio padre
# print(path.parent.parent.parent)

# Path("python_course/rutas/01-path.py") # Linux
# Path(r"python_course\rutas\01-path.py") # Windows

# Path() # Directorio actual

# Path.home() # Directorio home

# Path.cwd() # Directorio actual

# print(Path.cwd()) # Directorio actual

# Path("python_course/rutas/01-path.py").exists() # Verificar si el archivo existe

# Path("python_course/rutas/01-path.py").is_dir() # Verificar si es un directorio

# Path("python_course/rutas/01-path.py").is_file() # Verificar si es un archivo

# Path("python_course/rutas/01-path.py").is_absolute() # Verificar si es una ruta absoluta

# Path("python_course/rutas/01-path.py").is_symlink() # Verificar si es un enlace simbólico


# home = Path.home() # Directorio home

# wave_absolute = Path(home, "ocean", "wave.txt") # Crear una ruta absoluta

# print(wave_absolute)

# print(home)

# shark = Path(Path.home(), "ocean", "animals", Path("fish", "shark.txt")) # Crear una ruta absoluta
# print(shark)

# wave = Path("ocean","sea", "wave.txt")
# tides = wave.with_name("tides.txt") # Cambiar el nombre del archivo (Cambia el nombre del ultimo str en la ruta)
# print(wave)
# print(tides)


# for txt_path in Path.cwd().glob("*.gitignore"): # Buscar en el directorio actual
#     print(txt_path)

# for txt_path in Path.cwd().glob("**/*.txt"): # Buscar en todos los subdirectorios
#     print(txt_path)

# shark = Path("ocean", "animals", "fish", "shark.txt") # Ruta relativa
# below_ocean = shark.relative_to(Path("ocean")) # Ruta relativa
# below_animals = shark.relative_to(Path("ocean", "animals")) # Ruta relativa
# print(shark)
# print(below_ocean)
# print(below_animals)