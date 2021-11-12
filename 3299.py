n_input = int(input())

n = n_input
digito_anterior = -1
azarado = False
while n != 0:

    digito = n % 10
    n = int(n/10)

    if digito == 1 and digito_anterior == 3:
        azarado = True
        break

    digito_anterior = digito

if azarado:
    print(f"{n_input} es de Mala Suerte")
else:
    print(f"{n_input} NO es de Mala Suerte")