t = int(input())

for i in range(t):

    ponto_inicial = int(input())

    v, a = map(int, input().split())

    arestas = set()

    for j in range(a):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        arestas.add((x, y))

    print(len(arestas) * 2)