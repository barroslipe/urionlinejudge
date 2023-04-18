o = input()
soma = quant = 0

for i in range(144):
    x =  float(input())

    if i//12 > i%12:
        soma += x
        quant += 1

print(f"{(soma if o == 'S' else soma/quant):.1f}")