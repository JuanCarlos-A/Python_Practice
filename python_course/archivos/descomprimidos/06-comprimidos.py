from pathlib import Path
from zipfile import ZipFile


# Escribir un archivo comprimido

with ZipFile("comprimidos.zip", "w") as zip:

    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "python_course/archivos/comprimidos.zip":
            zip.write(path)


# with ZipFile("python_course/archivos/comprimidos.zip") as zip:
#     print(zip.namelist())