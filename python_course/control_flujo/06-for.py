# for numero in range(0, 11, 2):
#     print(numero)

comparar = 11

for numero in range(11):
    print(numero) if numero == comparar else print(f'El número {numero} no es igual a {comparar}')


for numero in range(11):
    if numero == comparar:
        print("Encontrado : ", numero)
        break

else:
    print("No encontrado")


for char in "Ultimate Python Course":
    print(char)