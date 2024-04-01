def dividir(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre cero", f"el numero es {n}")
    return 5 / n

try:
    dividir()
except ZeroDivisionError as e:
    print(e)