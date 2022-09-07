n = int(input())

regras  = { 'ataque': ['pedra', 'papel'],
            'papel': [],
            'pedra': ['papel']
            }


for i in range(n):
    j1 = input()
    j2 = input()

    if j1 == j2:
        if j1 == 'papel':
            print('Ambos venceram')
        elif j1 == 'pedra':
            print('Sem ganhador')
        else:
            print('Aniquilacao mutua')
    else:
        if regras[j1].count(j2) > 0:
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')