n = int(input())
numeros = list(map(int, input().split()))

menor_valor = numeros[0]
posicao = 0

for i, numero in enumerate(numeros):
    if numero < menor_valor:
        menor_valor = numero
        posicao = i

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")