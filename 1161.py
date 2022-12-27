def fat(n):
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    else:
        ac = 1
        for i in range(2, n+1):
            ac *= i
        return ac

while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        exit(0)
    
    print(fat(a) + fat(b))