n = int(input())

for i in range(n):
    frase = input().lower()

    contagem = {}
    for el in frase:
        if 'a' <= el <= 'z':
            if el in contagem:
                contagem[el] = contagem.get(el) + 1
            else:
                contagem[el] = 1

    lista = list(contagem.items())

    for j in range(len(lista)-1):
        for k in range(len(lista)-j-1):
            if (lista[k][1] < lista[k+1][1]) or (lista[k][1] == lista[k+1][1] and lista[k][0] > lista[k+1][0]):
                lista[k], lista[k+1] = lista[k+1], lista[k]

    maior_valor = lista[0][1]

    for l in lista:
        if l[1] == maior_valor:
            print(l[0], end='')

    print()