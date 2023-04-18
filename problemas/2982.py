n = int(input())

gastos = verbas = 0
for i in range(n):
    t, c = input().split()

    if t == 'V':
        verbas += int(c)
    else:
        gastos += int(c)

if verbas >= gastos:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')