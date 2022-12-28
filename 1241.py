n = int(input())

for i in range(n):
    a, b = input().split()

    tamA = len(a)
    tamB = len(b)
    
    if tamB > tamA:
        print('nao encaixa')
    else:
        if b == a[tamA-tamB:]:
            print('encaixa')
        else:
            print('nao encaixa')