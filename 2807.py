n = int(input())

numeros = []
numeros.append(1)
numeros.append(1)
    
for i in range(2, n):
    numeros.append(numeros[i-1] + numeros[i-2])

if n == 1:
    print(1)
elif n == 2:
    print('1 1')
else:
    for i in range(n):
        print(numeros[n-i-1], end="")
        if i != n-1:
            print(' ', end="")
    print()