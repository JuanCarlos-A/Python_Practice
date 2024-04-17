from pathlib import Path

path = Path()

paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db" : "Base de datos",
    "api" : "API Rest",
    "graficos" : "Gráficos"
}

def load(p):
    paquete = __import__(str(p).replace("/", ".")) #__import__() importar de forma casera
    try:
        paquete.init(**dependencias) #init() es una función que se encuentra en __init__.py
    except Exception:
        print("El paquete no tiene funcion init()")

list(map(load, paths))


