import math

n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    rafael =  9 * x * x + y * y
    beto = 2 * x * x + 25 * y * y
    carlos =  -100 * x + y * y * y

    if rafael > beto:
        if rafael > carlos:
            print("Rafael ganhou")
        else:
            print("Carlos ganhou")
    elif beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")