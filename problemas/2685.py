while True:
    try:
        m = int(input())

        if m >= 0 and m < 90 or m == 360:
            print('Bom Dia!!')
        elif m >=90 and m < 180:
            print('Boa Tarde!!')
        elif m >= 180 and m <270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
    except EOFError:
        exit(0)