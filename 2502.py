while True:
    try:
        c, n = map(int, input().split())
    
    except EOFError:
        exit(0)
    
    cifras = []
    for i in range(2):
        cifras.append(input())
    
    dicionario = {}
    dicionario2 = {}
    for i in range(c):
        dicionario[cifras[0][i]] = cifras[1][i]
        dicionario2[cifras[1][i]] = cifras[0][i]

    texto = []
    for i in range(n):
        texto.append(input())
    
    for i in range(n):
        for j in texto[i]:
            if j.upper() in dicionario.keys():
                print(dicionario[j.upper()] if j.isupper() else dicionario[j.upper()].lower() , end="")
            elif j.upper() in dicionario2.keys():
                print(dicionario2[j.upper()] if j.isupper() else dicionario2[j.upper()].lower(), end="")
            else:
                print(j, end="")
        print()
    print()