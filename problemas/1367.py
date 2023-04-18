while True:
    n = int(input())

    if n == 0:
        exit(0)

    s = p = 0
    incorretos = {}
    for i in range(n):
        problema = input().split()

        if problema[2] == 'correct':
            s += 1
            p += int(problema[1])

            if incorretos.get(problema[0]):
                p += incorretos.get(problema[0]) * 20

        else:
            valor = 0
            if incorretos.get(problema[0]):
                valor = incorretos.get(problema[0])

            incorretos[problema[0]] = valor + 1
    
    print(s, p)