while True:

    try:
        n, gameplay = map(int, input().split())
    except EOFError:
        exit(0)

    publicados = 0
    for i in range(n):
        item, tipo = map(int, input().split())

        if gameplay == item and tipo == 0:
            publicados += 1

    print(publicados)