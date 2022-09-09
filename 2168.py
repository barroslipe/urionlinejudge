n = int(input())

matriz = []

for i in range(n+1):
    matriz.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matriz[i+1][j] + matriz[i][j+1] + matriz[i][j] + matriz[i+1][j+1] >= 2:
            print('S', end="")
        else:
            print('U', end="")
    print()