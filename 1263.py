while True:
    try:
        frase = input().split()
    except EOFError:
        exit(0)
    
    sequencia = False
    aliteracao = 0
    for i in range(len(frase) - 1):
        if frase[i][0].lower() == frase[i+1][0].lower():
            sequencia = True
        else:
            if sequencia:
                aliteracao += 1
            sequencia = False
    
    if sequencia:
        aliteracao += 1

    print(aliteracao)