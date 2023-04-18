e, f, c = map(int, input().split())

bebeu = 0
vazias = e + f

while vazias//c > 0:

    cheias = vazias//c
    bebeu += cheias
    vazias = cheias + vazias%c

print(bebeu)