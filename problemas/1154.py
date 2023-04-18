soma = count = 0

idade = int(input())

while idade > 0:

    soma += idade
    count += 1

    idade = int(input())

print(f"{soma/count:.2f}")