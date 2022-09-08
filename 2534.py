while True:
    try:
        n, q = map(int, input().split())
    except EOFError:
        exit(0)

    notas = []

    for i in range(n):
        nota = int(input())
        notas.append(nota)

    notas.sort(reverse=True)

    for i in range(q):
        consulta = int(input())

        print(notas[consulta-1])