frase = input().split()

for el, f in enumerate(frase):
    if len(f) >= 4 and f[0:2] == f[2:4]:
        frase[el] = f[2::]

print(*frase)