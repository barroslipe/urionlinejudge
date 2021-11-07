c = int(input())

for i in range(0, c):
    lista = list(map(int, input().split()))

    media = sum(lista[1:])/lista[0]

    quantidade = sum(j > media for j in lista[1:])

    print("%.3f%%" % (quantidade*100/lista[0]))