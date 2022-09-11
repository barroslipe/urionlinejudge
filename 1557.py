while True:

    n = int(input())

    if n == 0:
        exit(0)

    expo = 0
    deslocamento = len(str(2**((n-1)*2)))
    for i in range(n):
        for j in range(n):
            print("{result:>{deslocamento}}".format(result=2**(expo+j), deslocamento=deslocamento), end="")
            if j != n-1:
                print(' ', end="")
        print()
        expo +=1
    print()