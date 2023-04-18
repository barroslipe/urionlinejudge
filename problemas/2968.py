from math import ceil


v, n = map(int, input().split())

total_placas = v*n

for i in range(1, 10):
    print(ceil(i/10*total_placas), end="")
    if i != 9:
        print(' ', end="")
print()