while True:
    try:
        frase = list(input())
    except EOFError:
        exit(0)
    
    italico = negrito = False
    
    for i in range(len(frase)):
        if frase[i] == '_':
            if italico:
                frase[i] = '</i>'
            else:
                frase[i] = '<i>'

            italico = not italico

        elif frase[i] == '*':
            if negrito:
                frase[i] = '</b>'
            else:
                frase[i] = '<b>'

            negrito = not negrito
    
    print(*frase, sep='')