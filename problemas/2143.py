while True:
    t = int(input())

    if t == 0 :
        exit(0)

    for i in range(t):
        mesa = int(input())

        if mesa % 2 == 0:
            print(2 + (mesa -2)*2)
        else:
            print(1 + (mesa - 1)*2)