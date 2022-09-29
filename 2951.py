n, g = map(int, input().split())

runas = {}
for i in range(n):
    ri, vi = input().split()
    runas.update({ri: int(vi)})

x = int(input())
recital = input().split()

soma = 0
for i in recital:
    soma += runas[i]

print(soma)
print('My precioooous' if soma < g else 'You shall pass!')