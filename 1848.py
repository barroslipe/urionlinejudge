import math

soma = 0
while True:
    try:
        entrada = input()
    except EOFError:
        break

    if entrada == 'caw caw':
        print(f"{soma:.0f}")
        soma = 0
    else:
        for i, item in enumerate(entrada[::-1]):
            if item == '*':
                soma += math.pow(2, i)