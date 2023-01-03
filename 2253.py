while True:
    try:
        senha = input()
    except EOFError:
        exit(0)
    

    possui_maiuscula = possui_minuscula = possui_numero = False
    nao_possui_pontuacao_acentuacao_espaco = True
    tam_minimo = 6
    tam_maximo = 32

    if tam_minimo > len(senha) or len(senha) > tam_maximo:
        print('Senha invalida.')
    else:
        for s in senha:
            if s.isdigit():
                possui_numero = True
            elif 'a' <= s <= 'z':
                possui_minuscula = True
            elif 'A' <= s <= 'Z':
                possui_maiuscula = True
            else:
                nao_possui_pontuacao_acentuacao_espaco = False

        if possui_numero and possui_minuscula and possui_maiuscula and nao_possui_pontuacao_acentuacao_espaco:
            print('Senha valida.')
        else:
            print('Senha invalida.')