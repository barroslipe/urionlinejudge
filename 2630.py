t = int(input())

for i in range(1, t+1):
    op = input()

    r, g, b = map(int, input().split())

    if op == 'eye':
        print(f'Caso #{i}: {int(0.3*r + 0.59*g + 0.11*b)}')
    elif op == 'mean':
        print(f'Caso #{i}: {(r + g + b) // 3}')
    elif op == 'min':
        if r < g:
            if r < b:
                print(f'Caso #{i}: {r}')
            else:
                print(f'Caso #{i}: {b}')
        else:
            if g < b:
                print(f'Caso #{i}: {g}')
            else:
                print(f'Caso #{i}: {b}')
    else:
        if r > g:
            if r > b:
                print(f'Caso #{i}: {r}')
            else:
                print(f'Caso #{i}: {b}')
        else:
            if g > b:
                print(f'Caso #{i}: {g}')
            else:
                print(f'Caso #{i}: {b}')