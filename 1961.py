import math


p, n = map(int, input().split())

canos = list(map(int, input().split()))

venceu = True

for i in range(len(canos) - 1):
    if p < abs(canos[i+1] - canos[i]):
        venceu = False
        break

if venceu:
    print("YOU WIN")
else:
    print("GAME OVER")