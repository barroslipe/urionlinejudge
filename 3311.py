n = int(input())

empregados = []

for i in range(n):
    empregados.append(input())

for j in range(len(empregados)-1):
    for k in range(len(empregados)-1-j):
        if empregados[k][0] > empregados[k+1][0]:
            empregados[k], empregados[k+1] = empregados[k+1], empregados[k]

print(*empregados, sep='\n')