from collections import deque

fila = deque([1, 2])

print(fila)

fila.append(3)

print(fila)

fila.popleft()
fila.popleft()
fila.popleft()

print(fila)

print("La fila está vacía") if not fila else print("La fila tiene elementos")
