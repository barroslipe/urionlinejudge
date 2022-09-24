def mdc (a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


n = int(input())

entrada = list(map(int, input().split()))
entrada.sort()

saida = entrada[-1] + 1

while True:

    coprimo = True
    for el in entrada:
        if mdc(saida, el) != 1:
            coprimo = False
            break
    
    if coprimo:
        print(saida)
        exit(0)
    
    saida += 1