n = int(input())

for i in range(n):
    a, b = map(int, input().split('x'))

    if a != b:
        for j in range(5, 11):
            print(f'{a} x {j} = {a*j} && {b} x {j} = {b*j}')
    else:
        for j in range(5, 11):
            print(f'{a} x {j} = {a*j}')