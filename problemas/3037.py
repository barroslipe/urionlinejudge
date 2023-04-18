n = int(input())


for i in range(n):
    pontuacao = []
    for j in range(2):
        pontos  = 0
        for k in range(3):
            x, d = map(int, input().split())
            
            pontos += x*d
        
        pontuacao.append(pontos)

    if pontuacao[0] < pontuacao[1]:
        print('MARIA')
    else:
        print('JOAO')