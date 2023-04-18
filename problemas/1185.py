o = input()

soma = quant = 0

for i in range(144):
    x = float(input())

    if i//11 <= i%11:
        soma += x
        quant += 1

print(f"{(soma if o == 'S' else soma/quant):.1f}")