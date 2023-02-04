n = int(input())

for i in range(n):
    itens =  set(input().split())

    l_ordenada = sorted(list(itens))

    print(*l_ordenada)