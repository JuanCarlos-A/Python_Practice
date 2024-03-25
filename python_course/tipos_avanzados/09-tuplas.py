numeros = (1, 2, 3) + (4, 5, 6) # Concatenacion de tuplas

print(numeros)

lista = list(numeros) # Convertir tupla a lista usando el constructor list

print(lista)

print(numeros[:2]) # Slicing de tuplas

primero, segundo, *otros = numeros # Desempaquetado de tuplas

print(primero, segundo, otros) # 1 2 [3, 4, 5, 6]

for n in numeros:
    print(n)

print(x for x in numeros) # Generador

new_list = [x for x in numeros if x > 4]

