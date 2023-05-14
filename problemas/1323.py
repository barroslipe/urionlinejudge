while True:

    n = int(input())

    if n == 0:
        break

    saida = 0

    while n != 0:
        saida += n*n
        n -= 1
    
    print(saida)