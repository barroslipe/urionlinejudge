from math import sqrt


n = int(input())

posicoes = []
for i in range(n):
    posicoes.append( list(map(int, input().split())) )

for i in range(n):
    menor_distancia = -1
    for j in range(n):
        if i == j:
            continue
        
        distancia = sqrt( (posicoes[i][0] - posicoes[j][0])**2 + (posicoes[i][1] - posicoes[j][1])**2 + (posicoes[i][2] - posicoes[j][2])**2)

        if menor_distancia == -1 or distancia < menor_distancia:
            menor_distancia = distancia
    
    if menor_distancia <= 20:
        print('A')
    elif 20 < menor_distancia <= 50:
        print('M')
    else:
        print('B')