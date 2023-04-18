n = int(input())
posicao = input()

copos = [0, 0, 0]

if posicao == 'A':
    copos[0] = 1
elif posicao == 'B':
    copos[1] = 1
else:
    copos[2] = 1


for i in range(n):
    mov = int(input())

    if mov == 1:
        copos[0],  copos[1] = copos[1], copos[0]
    elif mov  == 2:
        copos[1],  copos[2] = copos[2], copos[1]
    else:
        copos[0],  copos[2] = copos[2], copos[0]


if copos[0] == 1:
    print('A')
elif copos[1] == 1:
    print('B')
else:
    print('C')