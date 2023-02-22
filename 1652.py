l, n =  map(int, input().split())

dicionario = {}
for i in range(l):
    a, b = input().split()
    dicionario[a] = b

for i in range(n):
    palavra = input()

    if palavra in dicionario:
        print(dicionario[palavra])
    elif palavra[-1] == 'y' and (palavra[-2].isalpha() and palavra[-2] not in ('a', 'e', 'i', 'o', 'u')):
        print(palavra[:-1] + 'ies')
    elif palavra[-1] == 'o' or palavra[-1] == 's' or palavra[-1] == 'x' or palavra[-2:] == 'ch' or palavra[-2:] == 'sh':
        print(palavra + 'es')
    else:
        print(palavra + 's')