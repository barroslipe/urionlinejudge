n, m =  map(int, input().split())

imperio = []
for i in range(n):
    imperio. append(input().split())

coordenadas = '0 0';
for l in range(1, n-1):
    for c in range(1, m-1):
        if imperio[l][c] == '42':
            ##cima
            if (imperio[l-1][c-1] == '7' and imperio[l-1][c] == '7' and imperio[l-1][c+1] == '7'
               and imperio[l][c-1] == '7' and imperio[l][c+1] == '7'
               and imperio[l+1][c-1] == '7' and imperio[l+1][c] == '7' and imperio[l+1][c+1] == '7'):
               coordenadas = ""+str(l+1) + " " + str(c+1)

print(coordenadas)