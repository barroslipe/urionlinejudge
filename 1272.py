n = int(input())

for i in range(n):
    frase = input().split()

    for palavra in frase:
        print(palavra[0], end='')
    print()