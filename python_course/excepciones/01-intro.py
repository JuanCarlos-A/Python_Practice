try:
    numero1 = int(input("Ingresa el primer numero: "))
except ValueError as ve:
    print(f"Ocurrio un error : {ve}")
