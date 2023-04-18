n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x

    soma = 0
    for j in range(x+1, y):
        if j % 2 != 0:
            soma += j

    print(soma)
