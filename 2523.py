while True:
    try:
        alfabeto = input()

        n = int(input())
        lampadas = list(map(int, input().split()))
    except EOFError:
        exit(0)

    for i in lampadas:
        print(alfabeto[i-1], end="")
    print()