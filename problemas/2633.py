while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    churrasco = {}

    for i in range(n):
        carne, validade = input().split()

        churrasco[carne] = int(validade)
    
    ordenada = sorted(churrasco.items(), key= lambda x: x[1])

    for index in range(len(ordenada)):
        print(ordenada[index][0], end ='')
    
        if index != len(ordenada) - 1:
            print(' ', end='')

    print()