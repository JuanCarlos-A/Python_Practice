from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")

# archivo.exists() # True

# archivo.is_file() # True

# archivo.rename()

# archivo.unlink()

# print(archivo.stat())

print("Acceso : ", ctime(archivo.stat().st_atime))
print("Creacion : ", ctime(archivo.stat().st_ctime))
print("Modificacion : ", ctime(archivo.stat().st_mtime))

