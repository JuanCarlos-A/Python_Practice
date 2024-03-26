pila = []

pila.append(1)
pila.append(2)

print(pila)

ultimo_elemento_eliminado = pila.pop()

print(ultimo_elemento_eliminado)

pila.pop()
pila.pop()

print(pila)

print("La pila esta vacia") if not pila else print("La pila no esta vacia")
