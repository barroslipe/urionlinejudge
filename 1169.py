import math

n =  int(input())

q = 2
a1 = 1

for i in range(0, n):
    x = int(input())

    soma = a1 * (math.pow(2, x) - 1)  / (q - 1)

    soma = soma / 12

    soma = soma / 1000

    print("%i kg" % soma)