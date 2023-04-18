while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    print(n-1)