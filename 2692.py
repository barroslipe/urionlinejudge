dic = {}

n, m = map(int, input().split())

for i in range(n):
    a, b = input().split()

    dic[a] = b
    dic[b] = a

for i in range(m):
    frase = input()

    for f in frase:
        if f in dic:
            print(dic[f], end='')
        else:
            print(f, end='')
    print()