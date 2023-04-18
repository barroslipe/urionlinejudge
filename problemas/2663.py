n = int(input())
vagas = int(input())

notas = []
for i in range(n):
    notas.append(int(input()))

notas.sort(reverse=True)

empatados = 0

for el in notas[vagas:]:
    if notas[vagas-1] == el:
        empatados += 1

print(vagas + empatados)