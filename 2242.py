sequencia = []
vogais = ['a', 'e', 'i', 'o', 'u']

risada = input()

for i in risada:
    if i in vogais:
        sequencia.append(i)

if sequencia == sequencia[::-1]:
    print('S')
else:
    print('N')