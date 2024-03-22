""" Retorno de valores """

def suma(a :int, b: int) -> int:
    """ Realiza la suma de dos números 
    Args:
        a (int): Primer número
        b (int): Segundo número
    Returns:
        int: Suma de los dos números
    """
    resultado = a + b
    return resultado

c = suma(1, 2)
d = suma(c, 2)

print(d) # 5
