n = int(input())

for i in range(n):
    linha = list(map(int, input().split()))

    n_jogadores = int(linha.pop(0))
    
    linha.sort()

    print(f"Case {i+1}: {linha[n_jogadores//2]}")