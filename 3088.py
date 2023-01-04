while True:
    try:
        frase = input()
    except EOFError:
        exit(0)
    
    for i in range(len(frase)):
        if frase[i] == ' ' and (i!= len(frase) and (frase[i+1] == ',' or frase[i+1] == '.')):
            continue
        else:
            print(frase[i], end='')


    print()