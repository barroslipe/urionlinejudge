while True:
    try:
        palavra = input()
    except EOFError:
        exit(0)

    tam = len(palavra)

    for i in range(tam):
        saida = palavra[:tam - i]
        for el, s in enumerate(saida):
            if el != 0:
                print('',s, end='')
            else:
                for x in range(i):
                    print(' ', end='')
                print(s, end='')
        print()
    print()