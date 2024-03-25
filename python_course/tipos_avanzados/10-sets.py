numeros = {1, 2, 3, 4, 5}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_set = {x for x in lista}

# print(numeros | new_set)

# print(numeros & new_set)

print(numeros - new_set)

print(numeros ^ new_set)

if 5 in new_set:
    print("5 is in the set")