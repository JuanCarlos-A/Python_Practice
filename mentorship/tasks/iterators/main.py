"""Iterators and Iterables"""

lista = [x for x in range(10)] # Iterable

# Iterating over a list

for i in lista:
    print(i)


iterador = iter(lista) # Iterator

print(iterador)

print(next(iterador))

