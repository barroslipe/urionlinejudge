n = int(input())

consultas = []
for i in range(n):
    consultas.append(input())

q = int(input())

for i in range(q):
    palavra = input()

    cont = 0
    maior = 0
    for j in consultas:
        if j.find(palavra, 0, len(palavra)) != -1:
            cont += 1
            if len(j) > maior:
                maior = len(j)
    
    if cont != 0:
        print(cont, maior)
    else:
        print(-1)