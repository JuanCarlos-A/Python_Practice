n1 = float(input('Digita el primer número: ')) # Se pide al usuario que digite el primer número
n2 = float(input('Digita el segundo número: ')) # Se pide al usuario que digite el segundo número y se convierte a flotante

suma = n1 + n2 # Se realiza la suma de los dos números

resta = n1 - n2 # Se realiza la resta de los dos números

multiplicacion = n1 * n2 # Se realiza la multiplicación de los dos números

division = n1 / n2 # Se realiza la división de los dos números

mensaje = f"""
La suma de {n1} y {n2} es: {suma}
La resta de {n1} y {n2} es : {resta}
La multiplicación de {n1} y {n2} es: {multiplicacion}
La división de {n1} y {n2} es: {division}
"""

print(mensaje) # Se imprime el mensaje con los resultados de las operaciones

# print(round((n1).__add__(n2))) # Se imprime la suma de los dos números usando el método __add__ de la clase float
