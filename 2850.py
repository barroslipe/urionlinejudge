while True:
    try:
        posicao = input()
    except EOFError:
        exit(0)
    
    if posicao == 'esquerda':
        print('ingles')
    elif posicao == 'direita':
        print('frances')
    elif posicao == 'nenhuma':
        print('portugues')
    else:
        print('caiu')