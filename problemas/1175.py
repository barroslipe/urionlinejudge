vetor = []

for i in range(20):
    x = int(input())
    vetor.append(x)

for i in range(10):
    vetor[i], vetor[19-i] = vetor[19-i], vetor[i]

for i in range(20):
    print(f"N[{i}] = {vetor[i]}")