#Forma 1
# def suma(*numeros :float) -> None: # *numeros es una tupla
#     print(sum(x for x in numeros))  # sum() es una función que suma los elementos de un iterable (lista, tupla, etc)

# suma(2, 5, 10)

def suma(*numeros :float) -> None:
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 10)