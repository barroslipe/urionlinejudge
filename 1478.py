while True:
    n = int(input())

    if n == 0:
        exit()

    for l in range(1, n+1):
        for c in range(1, n+1):
            print(f"{abs(l-c)+1:>3}", end="")
            if c != n:
                print(' ', end="")
        print()

    print()