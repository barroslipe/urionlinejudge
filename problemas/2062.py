n = int(input())
palavras = input().split()

for i, p in enumerate(palavras):
    if len(p) == 3:
        if p[:2] == 'OB':
            print('OBI', end='')
        elif p[:2] == 'UR':
            print('URI', end='')
        else:
            print(p, end='')
    else:
        print(p, end='')
        
    if i != len(palavras) - 1:
            print(' ', end='')
print()