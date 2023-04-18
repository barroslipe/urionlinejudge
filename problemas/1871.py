while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        exit(0)
    
    soma = str(m + n)

    
    saida = filter( lambda el: el != '0', soma)
    print(*saida, sep='')
