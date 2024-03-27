try:
    number = int(input("Ingresa un numero: "))
    print(number)
except ValueError as ve:
    print("No ingresaste un numero", ve)
else:
    print("Todo salio bien")
finally:
    print("Fin del programa")


try:
    number = 1000
    num = number / 0
    print(num)
except ZeroDivisionError:
    print("No puedes dividir por cero")

try:
    numero = 6
    texto = "Hola"
    suma = numero + texto
    print(suma)
except TypeError:
    print("No puedes sumar un numero con un texto")
finally:
    print("Fin del programa")


lista = [1, 2, 3]

try:
    print(lista[3])
except IndexError:
    print("No existe ese indice")


class ExampleError(Exception):
    pass


class C(ExampleError):
    pass

class D(C):
    pass

for cls in [C, D, ExampleError]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except ExampleError:
        print("ExampleError")