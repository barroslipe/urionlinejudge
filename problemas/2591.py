c = int(input())

for i in range(c):
    palavra = input()

    cont = 0
    operandos = []
    for l in palavra:
        if l == 'a':
            cont += 1
        else:
            if cont != 0:
                operandos.append(cont)
            cont = 0
    
    print('k', end='')
    for j in range(operandos[0]*operandos[1]):
        print('a', end='')

    print()