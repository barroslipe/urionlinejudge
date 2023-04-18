nomes = []
while True:
    try:
        nomes.append(input())
    except EOFError:
        break


for i in range(len(nomes) - 1):
    for j in range(len(nomes) - 1 - i):
        if nomes[j].lower() > nomes[j+1].lower():
            nomes[j], nomes[j+1] = nomes[j+1], nomes[j]

print(nomes[-1])