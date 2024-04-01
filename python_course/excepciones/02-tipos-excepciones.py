try:
    numero1 = int(input("Ingresa el primer numero: "))
    # weweew
except ValueError as e:
    print(f"Ocurrio un error : {e}. Este error es de tipo")
except Exception as e:
    print(f"Ocurrio un error de tipo: {type(e)}")
