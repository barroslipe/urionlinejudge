n = int(input())

for i in range(n):
    trapaceou = False

    dieta = input()
    cafe_da_manha = input()
    almoco = input()

    comeu = cafe_da_manha + almoco

    for c in comeu:
        if c not in dieta:
            trapaceou = True
            break

    if not trapaceou:

        jantar = ''
        for d in dieta:
            if d not in comeu:
                jantar += d

        print(''.join(sorted(jantar)))
    else:
        print('CHEATER')