n, m = map(int, input().split())

jogadores_gols = 0

for i in range(n):
    partidas = input().split()

    fez = True
    for p in partidas:
        if p ==  '0':
            fez = False
            break

    if fez:
        jogadores_gols += 1

print(jogadores_gols)