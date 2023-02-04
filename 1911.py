

while True:

    n = int(input())

    if n == 0:
        exit(0)

    banco_de_dados = {}
    falsas = 0

    for i in range(n):
        nome, assinatura = input().split()

        banco_de_dados[nome] = assinatura

    m = int(input())

    for i in range(m):
        nome, assinatura = input().split()

        assinatura_oficial = banco_de_dados[nome]

        diferencas = 0
        for j in range(len(assinatura)):
            if assinatura[j] != assinatura_oficial[j]:
                diferencas += 1

        if diferencas > 1:
            falsas += 1

    print(falsas)