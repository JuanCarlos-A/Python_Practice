def hola(first_name:str, last_name:str = "Aguilar") -> None:
    print("Hola Mundo")
    print("Python Course")
    print(f'Hola {first_name} {last_name}')

hola("Juan")

hola(last_name="Perez", first_name="Juan")