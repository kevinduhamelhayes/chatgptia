from collections import deque

fila=deque(list (range(1, 100)))
fila.append(1)
fila.append(2)
print(fila)
fila.popleft()
print(fila)
