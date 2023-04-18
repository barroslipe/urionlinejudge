cont = 0
while True:
    m = int(input())

    if m == 0:
        exit(0)
    
    cont  += 1
    equacao = input()

    partes = []
    operando = ''
    for i in equacao:

        if i == '+' or  i == '-':
            partes.append(int(operando))
            operando = ''
            partes.append(i)
        else:
            operando += i

    partes.append(int(operando))
    
    total = 0
    soma = True
    for j in partes:
        if j == '+':
            soma = True
        elif j == '-':
            soma = False
        elif soma:
            total += j
        else:
            total -= j

    print(f'Teste {cont}')
    print(f'{total}')
    print()