while True:
    try:
        n1, n2 = map(int, input().split())
    except EOFError:
        exit()

    campo = []
    tempo = 0

    for i in range(n1):
        e = input().split()
        campo.append(e)

    origem = []
    destino = []

    for l in range(n1):
        for c in range(n2):
            if campo[l][c] == '1':
                origem = [l, c]
            if campo[l][c] == '2':
                destino = [l, c]


    tempo = abs(destino[0]-origem[0]) + abs(destino[1]-origem[1])

    print(tempo)