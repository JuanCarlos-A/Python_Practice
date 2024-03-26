lista = [1, 2, 3, 4, 5]

lista2 = [6, 7]

lista_combinada = [*lista, *lista2]


dic = {"a" : 1, "b" : 4}
dic2 = {"b" : 2}

dic_combinado = {**dic, "c" : 5,  **dic2}

print(lista_combinada)
print(dic_combinado)
