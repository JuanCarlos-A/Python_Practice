try:
    numero1 = int(input("Ingresa el primer numero: "))
except Exception as e:
    print(f"Ocurrio un error de tipo: {type(e)}")
else:
    print("No ocurrio ningun error")
finally:
    print("Esto se ejecuta siempre.")

