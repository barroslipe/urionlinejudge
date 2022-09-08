caso = 1
while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    saida = '0'
    ocorrencias = 1

    if n != 0:
        for i in range(n+1):
            for j in range(i):
                saida += ' ' + str(i)
                ocorrencias += 1

        
    print(f"Caso {caso}: {ocorrencias} numero{'s' if ocorrencias > 1 else ''}")
    print(saida)
    print()
    
    caso += 1