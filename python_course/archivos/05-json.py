import json
from pathlib import Path

## Creamos una esctructura de datos parecida a un diccionario en fomato JSON

# productos = [
#     {"id":1, "nombre":"surfboard"},
#     {"id":2, "nombre":"bicicleta"},
#     {"id":3, "nombre":"skate"},
#     {"id":4, "nombre":"patines"},
# ]


## Crear un json

# data = json.dumps(productos)

# Path("python_course/archivos/productos.json").write_text(data)


## Leer json

data = Path("python_course/archivos/productos.json").read_text(encoding="utf-8")

productos = json.loads(data)


## Modificar Jason

productos[0]["name"] = "Chanchisto Feliz"

Path("python_course/archivos/productos.json").write_text(json.dumps(productos))
