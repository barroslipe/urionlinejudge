while True:
    try:
        t = int(input())
    except EOFError:
        exit(0)

    equacoes = []
    jogadores = []
    errados = []

    for i in range(t):
        equacoes.append(input().split())

    for i in range(t):
        l = input().split()
        jogadores.append([int(l[1]), l[0], l[2]])

    jogadores.sort()

    for i in range(t):
        
        a = int(equacoes[i][0])
        segunda_parte = equacoes[i][1].split('=')
        b = int(segunda_parte[0])
        c = int(segunda_parte[1])

        if jogadores[i][2] == '+':
            if a + b != c:
                errados.append(jogadores[i][1])
        elif jogadores[i][2] == '*':
            if a * b != c:
                errados.append(jogadores[i][1])
        elif jogadores[i][2] == '-':
            if a - b != c:
                errados.append(jogadores[i][1])
        else:
            if a + b == c or a * b == c or a - b == c:
                errados.append(jogadores[i][1])
    
    if len(errados) == 0:
        print('You Shall All Pass!')
    elif len(errados) == t:
        print('None Shall Pass!')
    else:
        errados.sort()
        print(*errados)