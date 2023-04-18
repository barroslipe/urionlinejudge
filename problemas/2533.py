while True:

    try:
        m = int(input())
    except EOFError:
        exit(0)

    numerador = denominador = 0

    for i in range(m):
        n, c = map(int, input().split())

        numerador += n*c
        denominador += c

    print(f"{numerador/ (denominador*100):.4f}")