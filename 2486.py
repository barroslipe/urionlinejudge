alimentos = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}

while True:

    t = int(input())

    if t == 0:
        exit(0)

    consumo = 0
    for i in range(t):
        entrada = input().split()
        quantidade = int(entrada[0])
        alimento = " ".join(entrada[1:])

        consumo += quantidade * alimentos[alimento]

    if consumo < 110:
        print(f'Mais {110 - consumo} mg')
    elif consumo > 130:
        print(f'Menos {consumo - 130} mg')
    else:
        print(f"{consumo} mg")