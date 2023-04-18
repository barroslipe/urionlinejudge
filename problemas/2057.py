s, t, f = map(int, input().split())

destino = s + t + f

if destino == 24:
    destino = 0
elif destino > 24:
    destino -= 24
elif destino < 0:
    destino += 24

print(destino)