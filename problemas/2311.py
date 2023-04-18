n = int(input())

for i in range(n):
    nome = input()
    dificuldade = float(input())
    notas = list(map(float, input().split()))

    notas.sort()

    nota = sum(notas[1:-1])

    print(f"{nome} {dificuldade*nota:.2f}")