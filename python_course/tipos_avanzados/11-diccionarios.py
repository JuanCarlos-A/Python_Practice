dicc = {"x" : 25, "y" : 50}

print(dicc)

print(dicc["x"])

print(dicc["y"])

dicc["z"] = 45 # Agregar un nuevo elemento al diccionario

if "w" in dicc.keys():
    print(f'El valor de w es: {dicc["w"]}')

print(dicc.get("w", "No existe la llave w en el diccionario")) # Si no existe la llave w, se imprime el mensaje

del dicc["z"]

del(dicc["y"])

print(dicc)

dicc["y"] = 30

print([x for x in dicc.keys()])

print([x for x in dicc.values()])

for key, value in dicc.items():
    print(f'La llave {key} tiene el valor {value}')

usuarios = [
    {"id" : 1, "nombre" : "Juan", "apellido" : "Perez"},
    {"id" : 2, "nombre" : "Maria", "apellido" : "Gomez"},
    {"id" : 3, "nombre" : "Pedro", "apellido" : "Jimenez"},
    {"id" : 4, "nombre" : "Ana", "apellido" : "Torres"},
    {"id" : 5, "nombre" : "Luis", "apellido" : "Gonzalez"},
    {"id" : 6, "nombre" : "Sofia", "apellido" : "Diaz"}
]

nombres = [x for x in [y["nombre"] for y in usuarios]]

print(nombres)
