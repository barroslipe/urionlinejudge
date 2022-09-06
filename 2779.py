n = int(input())
m = int(input())

figurinhas = []
for i in range(m):
    x = int(input())
    if figurinhas.count(x) == 0:
        figurinhas.append(x)

print(n - len(figurinhas))