
codigo = {}

for i in range(26):
    segredo = ''
    padrao = ''
    for j in range(i%3 + 1):
        padrao += '.'

    segredo += padrao
    for k in range(i//3):
        segredo += ' ' + padrao

    codigo.update({chr(97+i): segredo})


while True:
    try:
        n = int(input())
    except EOFError:
        exit()

    for i in range(n):
        letra = input()

        for k, v in codigo.items():
            if v == letra:
                print(k)
                break