n, m = map(int, input().split())

frutas = []
for i in range(n):
    frutas.append(input().lower())

arquivo = []
for j in range(m):
    arquivo.append(input().lower())


for fruta in frutas:
    tem_fruta = False
    fruta_reversa = fruta[::-1]
    for linha in arquivo:
        if linha.find(fruta_reversa) != -1 or linha.find(fruta) != -1: 
            print('Sheldon come a fruta', fruta)
            tem_fruta = True
            break

    if not tem_fruta:
        print('Sheldon detesta a fruta', fruta)