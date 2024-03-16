# Los nombres de las variables no pueden comenzar con numeros
# ERROR: 1nombre_variable = "Aprendiendo Python"


"""
Tipos de Datos principales definidos por Python

    Los Numeros: Dentro de esta categoria estan los int, float y los complejos

    Booleans: Estos tipos de datos implican una comparación o evaluación logica, esta True y False

    Secuencias: Son los datos ordenados. Aqui estan los:
        str o Strings = son cadenas de texto
        list = Con colecciones ordenadas y mutables []
        tuple = Son tuplas y su caracteristica es ser inmutables y ordenadas ()

    Conjuntos: Son colecciones de datos no ordenados
        Sets: Son colecciones de datos no ordenados {1,3,4},{"sasdad", "sa"}
        frozenSet: Son colecciones de datos no ordenadas e inmutables
            frozenset([1,2,4])

    Diccionarios: Son mapeos, tienen una llave y un valor que es representado por la llave
        dict = {}

    NoneType: Representa la ausencia del valor o valores nulos

"""

num = 1

print(type(num))

booleans = False

print(type(booleans))

strings = "Aprendiendo Python"

print(type(strings))

lista = [1, 2, 3]
for listas in lista:
    print(listas)

print(type(lista))

tupla = (1, 2, 3)

print(type(tupla))
for tuplas in tupla:
    print(tuplas)

dicccionario = {"nombre": "Juan", "edad": 18}

for clave, valor in dicccionario.items():
    print(f'La clave es {clave} y el valor {valor}') #Formats Strings

print(type(dicccionario))

nulos = None
print(nulos)
print(type(nulos))

valor_Set = {1,2,3}, {1,2,4}
print(valor_Set)

for clave in valor_Set:
    print(f'La clave es {clave} y el valor') 