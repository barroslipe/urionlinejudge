n = int(input())

for k in range(n):
    a, b = input().split()

    tamA = len(a)
    tamB = len(b)

    if tamA < tamB:
        print('nao encaixa')
    else:
        if b[-tamB:] == a[-tamB:]:
            print('encaixa')
        else:
            print('nao encaixa')