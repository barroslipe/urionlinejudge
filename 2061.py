n, m = map(int, input().split())

for i in range(m):
    op = input()

    if op == 'fechou':
        n += 1
    else:
        n -= 1
print(n)