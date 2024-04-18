from pathlib import Path

archivo = Path("python_course/archivos/archivo-prueba.txt")

texto = archivo.read_text()

print(texto)
