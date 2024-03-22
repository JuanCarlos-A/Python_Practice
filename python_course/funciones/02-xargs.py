""" Args in python """
#Forma 1
# def suma(*numeros :float) -> None: # *numeros es una tupla
#     print(sum(x for x in numeros))  # sum() es una función que suma los elementos de un iterable (lista, tupla, etc)

# suma(2, 5, 10)

def suma(*numeros :tuple) -> None: #Estos son xargs o args que reciben los parametros en forma de tupla
    """
    Suma los números que se pasen como argumentos, usando los args o xargs
    Args:
        *numeros (float): Números a sumar
    Returns:
        None
    
    Esta función recibe una cantidad indefinida de números y los suma, la cantidad de números que se reciben son una tupla
    """
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 10)
