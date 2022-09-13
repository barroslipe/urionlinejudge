
n = int(input())

votos = []
for i in range(n):
    votos.append(int(input()))

carlos = votos[0]
ganhou = True
for i in range(1, n):
    if carlos < votos[i]:
        ganhou = False
        break

if ganhou:
    print('S')
else:
    print('N')