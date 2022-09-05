n = int(input())

for i in range(n):
    t = int(input())

    saida = 2015 - t

    if saida <= 0:
        saida = abs(saida) + 1
        print(f"{saida} A.C.")
    else:
        print(f"{saida} D.C.")