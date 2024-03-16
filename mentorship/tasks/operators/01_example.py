# Operadores aritméticos
num1 = 10
num2 = 5

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modular = num1 % num2
elevar = num1 ** num2
division_resultado_entero = num1 // num2

print("suma:", suma)
print("resta:", resta)
print("multiplicacion:", multiplicacion)
print("division:", division)
print("modular:", modular)
print("elevar:", elevar)
print("reultado de la division en entero:", division_resultado_entero)

# Operadores de relacion
num3 = 7
num4 = 7

print("Igual:", num3 == num4)
print("No sean iguales:", num3 != num4)
print("Mayor que:", num3 > num4)
print("Menor que :", num3 < num4)
print("Mayor o igual que:", num3 >= num4)
print("Menor o igual que:", num3 <= num4)

# Operadores logicos
bool1 = True
bool2 = False

print("AND:", bool1 and bool2)
print("OR:", bool1 or bool2)
print("NOT:", not bool1) # False

# operadores de asignacion
x = 5
x += 3
print("x:", x)

y = 10
y -= 2
print("y:", y)

z = 7
z *= 2
print("z:", z)

# Operadores de Bits
a = 5
b = 3

c = a & b
d = a | b
e = a ^ b
f = ~a
g = a << 1
h = a >> 1

print(" AND:", c)
print(" OR:", d)
print(" XOR:", e)
print(" NOT:", f)
print("Mover a la izquierda:", g)
print("Mover a la derecha:", h)

# Operadores de identidad
i = 10
j = 10

print("is:", i is j)
print("is not:", i is not j)


# Operadores de Pertenencia
k = "Hola mundo"
print("in:", "mundo" in k)
print("not in:", "mundo" not in k)
