while True:
    
    n  = int(input())

    if n == 0:
        exit(0)
    
    for linha in range(1, n+1):
        for coluna in range(1, n+1):
            
                saida = 0

                if linha <= n/2:
                    a = linha
                else:
                    a = n + 1 - linha
                
                if coluna <= n/2:
                    b = coluna
                else:
                    b =  n + 1 - coluna

                if a <= b:
                    saida = a
                else:
                    saida = b
                
                if coluna != 1:
                    print(' ', end='')

                print(f"{saida:>3}", end='')

        print()
    print()