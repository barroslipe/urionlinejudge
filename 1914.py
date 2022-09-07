qt = int(input())

for i in range(qt):
    j1, esc1, j2, esc2 = input().split()
    n1, n2 = map(int, input().split())

    if (n1+n2)%2 == 0:
        if esc1 == 'PAR':
            print(j1)
        else:
            print(j2)
    else:
        if(esc1 == 'IMPAR'):
            print(j1)
        else:
            print(j2)