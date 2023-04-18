n = int(input())

bonecos = arquitetos = musicos = desenhistas = 0

for i in range(n):
    nome, setor, horas = input().split()

    horas = int(horas)

    if setor == 'bonecos':
        bonecos += horas
    elif setor == 'arquitetos':
        arquitetos += horas
    elif setor == 'musicos':
        musicos += horas
    else:
        desenhistas += horas

total = bonecos//8 + arquitetos//4 + musicos//6 + desenhistas//12

print(total)