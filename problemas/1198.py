while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        exit(0)

    print(abs(a-b))