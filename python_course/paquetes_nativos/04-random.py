import random
import string

lista = [1, 2, 3, 4, 5, 6, 7]

lista2 = [1, 2, 3, 4, 5, 6, 7]

random.shuffle(lista) # Toma una sequencia mutable y la des ordena de manera aleatoria

print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    "".join(random.choices("abecdefghi,.-*12345", k=5))
    
)

chars = string.ascii_letters
digitos = string.digits

seleccion = random.choices(chars + digitos, k=16)

print("".join(seleccion))

contrasena = "".join(random.choices(chars + digitos, k=16))

print(contrasena)
