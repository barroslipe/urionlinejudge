import math


n  = int(input())

quantidade_minima = n / math.log(n)

quantidade_maxima = 1.25506 * n / math.log(n)

print("%.1f %.1f" % (quantidade_minima, quantidade_maxima))