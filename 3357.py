import math


n, l, q = map(float, input().split())
n = int(n)

pessoas = input().split()

goles = int(l // q)

ultimo_gole = l%q

pessoa = 0

if ultimo_gole == 0:
    pessoa = (goles-1)%n
    ultimo_gole = q
else:
    pessoa = goles%n

print(f"{pessoas[pessoa]} {ultimo_gole:.1f}")