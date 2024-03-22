""" Kwargs in Python"""

def get_datos(**datos :dict) -> None:
    """ 
    Funcion para obtener datos de una persona

    Args: **datos (dict): Datos de la persona
    Returns: None

    Esta función recibe una cantidad indefinida de datos y los imprime, la cantidad de datos que se reciben son un diccionario
    """
    print({x : y for x, y in datos.items() if x == "nombre" or x == "apellido"}) #Llamar lso datos de nombre y apellido que son llaves
    print([x for x in datos.values() if x == "Juan" or x == "Perez"]) #Llamar los datos de nombre y apellido que son llaves
    print(datos)

get_datos(nombre = "Juan", apellido = "Perez", edad = 25, ciudad = "Quito")