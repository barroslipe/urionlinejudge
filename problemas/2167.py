n = int(input())
rotacoes = list(map(int, input().split()))
saida = 0

for i in range(n-1):
    if rotacoes[i] > rotacoes[i+1]:
        saida = i+1+1
        break

print(saida)