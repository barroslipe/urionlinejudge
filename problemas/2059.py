p, j1, j2, r, a = map(int, input().split())

if (j1+j2)%2 == 0:
    if p == 1:
        if a ==1 and r == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
    else:
        if a ==1 and r == 1:
            print('Jogador 2 ganha!')
        elif a == 1 and r == 0:
            print('Jogador 1 ganha!')
        elif a == 0 and r == 1:
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')
else:
    if p == 0:
        if a ==1 and r == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
    else:
        if a ==1 and r == 1:
            print('Jogador 2 ganha!')
        elif a == 1 and r == 0:
            print('Jogador 1 ganha!')
        elif a == 0 and r == 1:
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')