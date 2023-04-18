o = input()

soma = quant = 0

for i in range(12):
    for j in range(12):
        x = float(input())

        if j + i > 11:
            soma += x
            quant += 1

print(f"{(soma if o == 'S' else soma/quant):.1f}")