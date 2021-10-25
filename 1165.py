import math

n =  int(input())


for a in range(n):
    x = int(input())

    primo = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i == 0:
            print("%i nao eh primo" % x)
            primo = False
            break

    if primo:
        print("%i eh primo" % x)