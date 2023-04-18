n = int(input())

for i in range(n):
    s = input()

    valido = False

    if len(s) == 8:
        placa = s.split('-')
        if len(placa[0]) == 3 and len(placa[1]) == 4:

            verificacao = True
            for i in placa[0]:
                if not (i >= 'A' and i <= 'Z'):
                    verificacao = False
            for i in placa[1]:
                if not (i >= '0' and i <= '9'):
                    verificacao = False

            valido = verificacao

    if not valido:
        print('FAILURE')
        continue

    dig = int(s[-1])

    if dig == 1 or dig == 2:
        print('MONDAY')
    elif dig == 3 or dig == 4:
        print('TUESDAY')
    elif dig == 5 or dig == 6:
        print('WEDNESDAY')
    elif dig == 7 or dig == 8:
        print('THURSDAY')
    elif dig == 9 or dig == 0:
        print('FRIDAY')