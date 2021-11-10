x  =  int(input())

while x != 0:

    for i in range(1, x + 1):
        print(f"{i}", end="")

        if i != x:
            print(" ", end="")

    print()
    x  =  int(input())