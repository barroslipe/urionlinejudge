
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tam_alfabeto = len(alfabeto)

n = int(input())

for i in range(n):
    frase = input()

    alfabeto_temp = alfabeto.copy()
    for l in frase:
        if l in alfabeto_temp:
            alfabeto_temp.remove(l)

    tam_temp = len(alfabeto_temp)
    if tam_temp == 0:
        print('frase completa')
    elif tam_temp/tam_alfabeto <= 0.5:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
