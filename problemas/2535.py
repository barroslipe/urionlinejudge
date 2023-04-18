while True:
    try:
        n = input()
        if n == '':
            n = input()

        n = int(n)
    except EOFError:
        exit(0)

    saida = 0
    for i in range(n):
        especie = input()
        if especie == '':
            especie = input()

        raca = input()
        nome = input().split()

        if especie == 'cachorro' and len(nome) > 1:
            for x in nome:
                if x[0] == raca[0]:
                    saida += 1
                    break
    print(saida)