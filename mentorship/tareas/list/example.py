lista_normal = [2, 1, 3]
lista_normal.append(6) # [1, 2, 3, 4, 5, 6]
lista_normal.pop(0) # [2, 3, 4, 5, 6]
lista_normal.remove(3) # [2, 4, 5, 6]
lista_normal.insert(0, 1) # [1, 2, 4, 5, 6]
lista_normal.sort() # [1, 2, 4, 5, 6]

print(lista_normal)



lista_vacia = []

lista_iterable = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
