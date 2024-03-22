def hola(first_name:str, last_name:str = "Aguilar") -> None:
    """ 
    Funcion para saludar a una persona 
    Args: first_name (str): Nombre de la persona
          last_name (str): Apellido de la persona
    Author: Juan Aguilar
    Returns: None
    
    Es una funcion la cual permite saludar a una persona que ingrese su nombre y 
    apellido, en caso de que no ingrese el apellido se le asignara el apellido Aguilar
    como valor por defecto.
    """
    print("Hola Mundo")
    print("Python Course")
    print(f'Hola {first_name} {last_name}')

hola("Juan")

hola(last_name="Perez", first_name="Juan")