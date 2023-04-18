maior_palavra = ''

while True:
    frase = input().split()

    if frase[0] == '0':
        break
    
    for el, i in enumerate(frase):
        if el != 0:
            print('-', end='')
        
        if len(i) >= len(maior_palavra):
            maior_palavra = i
        print(len(i), end='')
    print()

print(f'\nThe biggest word: {maior_palavra}')