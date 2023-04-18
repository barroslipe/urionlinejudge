import math

n =  int(input())

for a in range(n):
    x = int(input())

    if ((x == 1) or (x == 2)):
        print("%i eh primo" % x)
    elif (x % 2) == 0:
        print("%i nao eh primo" % x)
    else:
        primo = True
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x%i == 0:
                print("%i nao eh primo" % x)
                primo = False
                break

        if primo:
            print("%i eh primo" % x)