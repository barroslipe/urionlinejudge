n = int(input())

for i in range(n):
    entrada = input()

    k = 0
    for l in entrada[::-1]:
        if l == '!':
            k += 1
        else:
            break
    
    n = int(entrada[:-k])

    saida = 1

    while n >=1:
        saida *= n
        n = n - k
    
    print(saida)