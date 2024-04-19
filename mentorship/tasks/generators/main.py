""" Generators 255"""



# Ejemplo 1

# def generator(maximo):
#     contador = 0

#     while contador < maximo:        
#         yield contador
#         contador += 1


# cantidad = generator(10)

# print(next(cantidad))

# for i in cantidad:
#     print(i)

# print(next(cantidad, "Se acabo")) # next(iterator, default)


# Ejemplo 2

# def fibonacci(maximo):
#     numeroA, numeroB = 0, 1

#     while numeroA < maximo:
#         yield numeroA
#         numeroA, numeroB = numeroB, numeroA + numeroB
    
#     return "Fin de la serie"


# for i in fibonacci(10):
#     print(i)


# Ejemplo 3

# array = (x for x in range(10))

# print(array)

# print(next(array, "Se acabo"))

# for i in array:
#     print(i)

# print(next(array, "Se acabo"))


# Ejemplo 4
# import sys
# import cProfile

# list_comprehension = [x for x in range(1000000)]

# generator_comprehension = (x for x in range(1000000))

# print(sys.getsizeof(list_comprehension))

# print(sys.getsizeof(generator_comprehension))

# cProfile.run('sum([x for x in range(1000000)])')

# cProfile.run('sum((x for x in range(1000000)))')


# Ejemplo 5

# def lista_al_cuadrado(nums_list):
#     for num in nums_list:
#         yield (num * num)

# lista = lista_al_cuadrado(x for x in range(10))

# for i in lista:
#     try:
#         if i == 25:
#             lista.throw(ValueError, "No se permite el numero 25 dentro de este ciclo") #Diferencia con raise
#             # lista.close()
#         print(i)
#     except ValueError:
#         print("No se permite el numero 25 dentro de este ciclo")
