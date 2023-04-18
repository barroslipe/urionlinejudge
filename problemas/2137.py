while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    cadastros = []
    for i in range(n):
        cadastros.append(input())
    
    for i in range(len(cadastros)-1):
        for j in range(len(cadastros)-i-1):
            if cadastros[j] > cadastros[j+1]:
                cadastros[j], cadastros[j+1] = cadastros[j+1], cadastros[j]
    
    print(*cadastros, sep='\n')