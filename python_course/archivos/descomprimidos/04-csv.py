import csv

## Write o Escribir

with open("python_course/archivos/archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "txt"])
    writer.writerow([1000, 1, "Esto es un twit sobre la comida"])
    writer.writerow([1001, 2, "Este twit contiene mucha informacion"])


## Leer o Reader

# with open("python_course/archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)

#     print(list(reader))

#     archivo.seek(0)

#     for linea in reader:
#         print(linea)


## Actualizar CSV
import os

with open("python_course/archivos/archivo.csv") as r, open("python_course/archivos/archivo_temporal.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea == []:
            continue
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Este twit contiene mucha informacion y ha sido actualizado"])
        else:
            writer.writerow(linea)

os.remove("python_course/archivos/archivo.csv")
os.rename("python_course/archivos/archivo_temporal.csv", "python_course/archivos/archivo.csv")
    
# for linea in reader:
#         if linea == []:
#             continue
#         if linea[0] == "1000":
#             writer.writerow([1000, 1, "Este twit contiene mucha informacion y ha sido actualizado"])
#         elif linea == "":
#             writer.writerow(linea)

