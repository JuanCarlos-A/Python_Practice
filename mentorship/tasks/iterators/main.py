"""Iterators and Iterables"""

# Example 1

# lista = [x for x in range(10)] # Iterable

# # Iterating over a list

# for i in lista:
#     print(i)


# iterador = iter(lista) # Iterator

# print(iterador)

# print(next(iterador))


# Example 2

# class Fibonacci:
#     def __init__(self, maximo):
#         self.maximo = maximo
#         self.numeroA = 0
#         self.numeroB = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.numeroA < self.maximo:
#             self.numeroA, self.numeroB = self.numeroB, self.numeroA + self.numeroB
#             return self.numeroA
#         else:
#             raise StopIteration
    
#     def __str__(self):
#         return "Fin de la serie"

# fibonacci = Fibonacci(10)

# for i in fibonacci:
#     print(i)


# Example 3

# class IteratorClass:
#     def __init__(self, coleccion):
#         self.coleccion = coleccion
#         self.indice = 0
    
#     def __iter__(self):
#         # print("Hola")
#         return self
    
#     def __next__(self):
#         if self.indice < len(self.coleccion):
#             self.indice += 1
#             print("Hola")
#             return self.coleccion[self.indice - 1]
#         else:
#             raise StopIteration


# objeto = IteratorClass([1, 2, 3, 4, 5])

# for i in objeto:
#     print(i)

# iterador = iter(objeto)

# while True:
#     try:
#         item = iterador.__next__()
#     except StopIteration:
#         break
#     else:
#         print(item)


# Example 4

from collections.abc import Iterator

class IteratorClass(Iterator):
    def __init__(self, coleccion):
        self.coleccion = coleccion
        self.indice = 0

    def __next__(self):
        if self.indice < len(self.coleccion):
            self.indice += 1
            return self.coleccion[self.indice - 1]
        else:
            raise StopIteration