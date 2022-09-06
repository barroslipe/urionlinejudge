porcoes = [300, 1500, 600, 1000, 150]
consumo = 0
for i in range(5):
    c = int(input())

    consumo += c*porcoes[i]

print(consumo + 225)