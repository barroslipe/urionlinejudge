while True:
    x, m = map(int, input().split())

    if x == 0 and m == 0:
        exit(0)

    print(x*m)