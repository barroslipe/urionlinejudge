while True:

    n = int(input())

    if n == 0:
        exit(0)
    
    comandos = input()

    direcao = 0
    for c in comandos:
        if c == 'D':
            direcao +=  1
        else:
            direcao -= 1

    if direcao%4 == 0:
        print('N')
    else:
        direcao = direcao%4

        if direcao in (-1, 3):
            print('O')
        elif direcao in (-2, 2):
            print('S')
        else:
            print('L')