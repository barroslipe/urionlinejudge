n = int(input())

for i in range(n):
    entrada = list(map(int, input().split()))

    soma = 0
    for i in range(1, len(entrada)):
        soma += entrada[i]
    
    print(soma - entrada[0] + 1)