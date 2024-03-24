mascotas = [
    ["Chancito", 3],
    ["Pelusa", 5],
    ["Firulais", 7],
    ["Rex", 2],
    ["Milo", 4],
    ["Toby", 6]
    ]

mascotas.sort(reverse=True, key = lambda x : x[1])

new_list = sorted(mascotas, key=lambda x : x[1])



#Metodo sin sort

# def ordena(elemento):
#     return elemento[1]

# #Aqui sort toma la referencia de la funcion ordena y la usa para ordenar la lista, 
# #pasandole cada elemento de la lista
# mascotas.sort(key=ordena)

