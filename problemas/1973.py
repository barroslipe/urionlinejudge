n = int(input())
linha = input().split()

estrelas = []
total_carneiros = 0
for i in linha:
    e = int(i)
    estrelas.append(e)
    total_carneiros += e

roubados = 0
pontos = 1
i = 0
while i >= 0 and i < n and estrelas[i] != 0:

    estrelas[i] -= 1
    roubados += 1    

    if estrelas[i]%2 == 0:
        i += 1
        pontos += 1
        if (i == n) or estrelas[i] == 0:
            pontos -= 1
    else:
        i -= 1
    
print(f"{pontos} {total_carneiros - roubados}")