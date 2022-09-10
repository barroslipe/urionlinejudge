n  = int(input())

carro = boneca = 0
for i in range(n):
    nome, sexo = input().split()

    if sexo == 'M':
        carro += 1
    else:
        boneca += 1

print(f'{carro} carrinhos')
print(f'{boneca} bonecas')