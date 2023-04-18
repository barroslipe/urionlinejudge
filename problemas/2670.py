andares = []

for i in range(3):
    andares.append(int(input()))

minutos = 0
min = 0
for andar in range(3):
    for i, pessoas in enumerate(andares):
        minutos += pessoas*abs(i - andar)*2
    if andar == 0 or minutos < min:
        min = minutos
    minutos = 0

print(min)