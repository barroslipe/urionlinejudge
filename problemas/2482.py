dicionario = {}

n = int(input())

for i in range(n):
    idioma = input()
    saudacao = input()

    dicionario[idioma] = saudacao

m = int(input())

for i in range(m):
    crianca = input()
    idioma = input()

    print(crianca)
    print(dicionario[idioma])

    print()