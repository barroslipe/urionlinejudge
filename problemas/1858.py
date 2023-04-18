n = int(input())
lista = map(int, input().split())

menor_valor = 21
posicao = 0

for i, e in enumerate(lista):
    if e < menor_valor:
        menor_valor = e
        posicao = i + 1

print(posicao)