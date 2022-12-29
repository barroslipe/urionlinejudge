while True:
    try:
        rastro = input()
        processos = int(input())
    except EOFError:
        exit(0)
    
    ciclos = 0
    sequencia = 0
    for leitura in rastro:
        if leitura == 'W':
            ciclos += 1

            if sequencia > 0:
                ciclos += sequencia//processos + ( 1 if sequencia%processos > 0 else 0 )

            sequencia = 0
        else:
            sequencia += 1

    if sequencia > 0:
        ciclos += sequencia//processos + ( 1 if sequencia%processos > 0 else 0 )

    print(ciclos)