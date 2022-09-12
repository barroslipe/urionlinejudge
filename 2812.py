from ast import Lambda


n  = int(input())

for i  in range(n):

    m = int(input())
    lista = list(map(int, input().split()))

    impares = [x for x in lista if x%2 != 0]

    impares.sort()

    if len(impares) == 0:
        print()
    else:

        menor = False
        i = 0
        for j in range(len(impares)):
            if menor:
                print(' ', end="")
                print(impares[i], end='')
                menor= not menor
                i += 1
            else:
                if i != 0:
                    print(' ', end="")
                print(impares[len(impares)-1-i], end='')
                menor= not menor

        print()