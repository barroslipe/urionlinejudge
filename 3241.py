n = int(input())

for i in range(n):
    equacao = list(input().split('+'))

    if equacao[0] == 'P=NP':
        print('skipped')
    else:
        print(int(equacao[0])+int(equacao[1]))