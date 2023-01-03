n = int(input())

vogais = ['a', 'e', 'i', 'o', 'u']


for i in range(n):
    
    cont = 0
    dificil = False
    palavra = input()
    for l in palavra:
        if l.lower() not in vogais:
            cont += 1

            if cont == 3:
                dificil = True
                break
        else:
            cont = 0
    
    if dificil:
        print(palavra, 'nao eh facil')
    else:
        print(palavra, 'eh facil')