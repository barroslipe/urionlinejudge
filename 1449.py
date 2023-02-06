t = int(input())

for i in range(t):

    dicionario = {}

    m, n = map(int, input().split())

    for j  in range(m):
        japones = input()
        portugues = input()

        dicionario[japones] = portugues
    
    for j in range(n):
        frase = input().split()

        for index, el in enumerate(frase):
            if el in dicionario:
                print(dicionario[el], end='')
            else:
                print(el, end='')

            if index != len(frase)-1:
                print(' ', end='')
    
        print()
    print()