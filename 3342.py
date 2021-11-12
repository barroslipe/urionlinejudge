n = int(input())

brancas = pretas = 0

if n % 2 == 0:
    brancas = pretas = n * n / 2
else:
    brancas = int(n * n / 2) + 1
    pretas = brancas -  1

print(f"{brancas:.0f} casas brancas e {pretas:.0f} casas pretas")