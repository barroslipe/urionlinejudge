from math import floor, sqrt


while True:

    entrada = list(map(int, input().split()))

    if entrada[0] == 0:
        exit(0)
    
    casa = entrada[0]*entrada[1]
    terreno_total = casa * 100/entrada[2]

    print(f"{floor(sqrt(terreno_total))}")