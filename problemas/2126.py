caso = 1

while True:
    try:
        n1 = input()
        n2 = input()
    except EOFError:
        exit(0)

    print(f'Caso #{caso}:')

    ocorrencia = posicao = 0

    for i in range(len(n2)-len(n1)+1):
        sub = n2[i:len(n1)+i] 
        if n1 == sub:
            ocorrencia += 1
            posicao = i+1

    if ocorrencia == 0:
        print('Nao existe subsequencia')
    else:
        print(f'Qtd.Subsequencias: {ocorrencia}')
        print(f'Pos: {posicao}')
    
    print()

    caso += 1