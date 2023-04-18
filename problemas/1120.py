while True:
    a, b = input().split()

    if a == '0' and b == '0':
        exit(0)
    
    saida = b.replace(a, '')
    print(0 if saida == '' else int(saida))
