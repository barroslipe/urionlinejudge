from math import sqrt


n = int(input())

print(f"{(((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**n)/sqrt(5):.1f}")