n =int(input())
paisagem = list(map(int, input().split()))


anterior = True
erro = False

for i in range(n-1):
    if paisagem[i] > paisagem[i+1] and (anterior or i == 0):
        anterior = False
    elif paisagem[i] < paisagem[i+1] and (not anterior or i == 0):
        anterior = True
    else:
        erro = True

if erro:
    print(0)
else:
    print(1)