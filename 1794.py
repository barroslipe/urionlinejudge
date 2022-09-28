n = int(input())

a, b = map(int, input().split())

if a <= n <= b:

    c, d = map(int, input().split())

    if c <= n <= d:
        print('possivel')
    else:
        print('impossivel')
else:
        print('impossivel')