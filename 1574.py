t = int(input())

for i in range(t):

    instrucoes = []
    saida = 0
    
    n = int(input())
    
    for j in range(n):
        instrucao = input()

        if instrucao.count('SAME'):
            instrucao = instrucoes[int(instrucao.split()[-1]) - 1]

        if instrucao ==  'LEFT':
            saida -= 1
        elif instrucao == 'RIGHT':
            saida += 1
        
        instrucoes.append(instrucao)
    
    print(saida)