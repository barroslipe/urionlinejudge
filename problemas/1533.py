while True:
    n = int(input())

    if n == 0:
        break

    assassinos = list(map(int, input().split()))

    maior = segundo_maior = -1
    i_maior = i_segundomaior = 0
    for i in range(n):
        if assassinos[i] > maior:
            maior, segundo_maior = assassinos[i], maior
            i_maior, i_segundomaior = i, i_maior
        elif assassinos[i] > segundo_maior:
            segundo_maior = assassinos[i]
            i_segundomaior = i
    
    print(i_segundomaior + 1)