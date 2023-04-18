while True:
    
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        exit(0)
    
    matriz = []
    for i in range(n):
        matriz.append(input())
    
    a, b = map(int, input().split())

    multiplo_linha = a//n
    multiplo_coluna = b//m

    for linha in matriz:
        for x in range(multiplo_linha):
            for l in linha:
                for y in range(multiplo_coluna):
                    print(l, end='')
            print()
    print()