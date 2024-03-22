""" Calculator Problem"""
print("Bienvenidos a la calculadora",
      " \nPara salir escribe Salir",
      "\nLas operaciones son suma, multi, div y resta"
      )

num = None

while True:
    if num is None:
        num = int(input("Introduce un número: "))
    operacion = input("Introduce la operación: ").capitalize().strip()
    if operacion == "Salir":
        break
    elif operacion == "Suma":
        num += int(input("Introduce otro número: "))
    elif operacion == "Resta":
        num -= int(input("Introduce otro número: "))
    elif operacion == "Multi":
        num *= int(input("Introduce otro número: "))
    elif operacion == "Div":
        num /= int(input("Introduce otro número: "))

    print(f"El resultado es: {num}")
