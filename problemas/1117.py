nota_valida = 0
soma = 0


while True:
    n = float(input())

    if n < 0 or n > 10:
        print('nota invalida')
    else:
        soma += n
        nota_valida += 1


    if nota_valida == 2:
        print(f"media = {soma/2}")
        break