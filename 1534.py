while True:
    try:
        n =  int(input())
    except EOFError:
        exit(0)

    for l in range(n):
        for c in range(n):
            if l + c == n - 1:
                print(2, end="")
            elif l == c:
                print(1, end="")
            else:
                print(3, end="")

        print()