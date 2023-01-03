while True:
    try:
        palavra = input()
        frase = input()
    except EOFError:
        exit(0)
    
    cont = 0
    for i in frase:
        if palavra.find(i) != -1:
            cont += 1
    print(cont)