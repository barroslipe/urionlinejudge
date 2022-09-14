n, c, m = map(int, input().split())

carimbadas = list(map(int, input().split()))

compradas = list(map(int, input().split()))

tenho = 0
for i in carimbadas:
    if i in compradas:
        tenho += 1

print(c - tenho)