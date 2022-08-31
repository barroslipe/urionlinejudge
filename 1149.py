soma = 0

entrada = list(map(int,input().split()))

a = entrada[0]
del entrada[0]

for i in entrada:
    if i > 0:
        n = i
        break

for i in range(0, n):
    soma += i + a

print(f"{soma}")