from pathlib import Path
from zipfile import ZipFile


## Escribir un archivo comprimido

# with ZipFile("comprimidos.zip", "w") as zip:

#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "python_course/archivos/comprimidos.zip":
#             zip.write(path)


with ZipFile("comprimidos.zip") as zip:
    print(zip.namelist())

    info = zip.getinfo("06-comprimidos.py")

    print(
        info.file_size,
        info.compress_size
    )

    zip.extractall("descomprimidos")