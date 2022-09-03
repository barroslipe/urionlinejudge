l = int(input())
t = input()

inicio = l*12
fim = inicio + 11

soma = 0


for i in range(144):
    x = float(input())

    if i >= inicio and i <= fim:
        soma += x

    if i > fim:
        print(f"{(soma if t == 'S' else soma/12):.1f}")
        break