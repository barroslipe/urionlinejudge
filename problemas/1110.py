from typing import Deque


n = int(input())

while n != 0:

    cartas = Deque(range(1, n + 1))

    descartadas = []
    while len(cartas) > 1:
        descartadas.append(cartas.popleft())
        cartas.append(cartas.popleft())

    print(f"Discarded cards: {str(descartadas)[1:-1]}")
    print(f"Remaining card: {cartas.popleft()}")
    
    n = int(input())