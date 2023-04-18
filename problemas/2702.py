a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

j = x - a
k = y - b
l = z - c

total = ( j if j > 0 else 0) + (k if k > 0 else 0) + (l if l > 0 else 0)

print(total)