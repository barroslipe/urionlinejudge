n = int(input())

while n != 0:    
    a = list(map(int, input().split()))

    a.sort()
    primeiro = segundo = 'x'

    i = 0
    while segundo == 'x':

        if i == (n - 1):
            segundo = a[i]
        else:
            if a[i] != a[i + 1]:
                if primeiro == 'x':
                    primeiro = a[i]
                    i += 1
                else:
                    segundo = a[i]
                    break
            else:
                i += 2

    print(f"{primeiro} {segundo}")

    try:
        n = int(input())
    except EOFError:
        break