def largo(texto :str) -> int:
    resultado = 0

    for _ in texto:
        resultado += 1
    return resultado
    
print("Cadena de caracteres")

lenght = largo("Hello World")

print(lenght)
