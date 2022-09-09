carros = turistas = 0

while True:

    entrada = input().split()

    if entrada[0] == 'ABEND':
        break

    movimento, pessoas = entrada[0], int(entrada[1])

    if movimento == 'SALIDA':
        turistas += pessoas
        carros += 1
    else:
        turistas -= pessoas
        carros -= 1

print(turistas)
print(carros)