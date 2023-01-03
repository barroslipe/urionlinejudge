def esta_formatada(registro):
    if len(registro) != 20 or registro[0:2] != 'RA':
        return False
    
    for r in registro[2::]:
        if int(r) > 18 or int(r) < 0:
            return False

    return True

n = int(input())

for i in range(n):
    registro = input()

    if not esta_formatada(registro):
        print('INVALID DATA')
    else:
        index = -1
        for el, r in enumerate(registro[2::]):
            if r != '0':
                index = 2 + el
                break
        print(registro[index::])