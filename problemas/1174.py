posicao = 0

while posicao < 100:

    x = float(input())

    if x <= 10:
        print(f"A[{posicao}] = {x:.1f}")

    posicao += 1