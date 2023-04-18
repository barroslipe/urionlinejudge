posicao = 0
maior_valor = int(input())

i = 1
while i < 100:

    n = int(input())

    if n > maior_valor:
        maior_valor = n
        posicao = i + 1

    i += 1

print(maior_valor)
print(posicao)