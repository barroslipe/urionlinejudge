par, impar, positivo, negativo = 0, 0, 0, 0

while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n != 0:
        if n < 0:
            negativo += 1
        else:
            positivo += 1

    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print("%i valor(es) par(es)" % par)
print("%i valor(es) impar(es)" % impar)
print("%i valor(es) positivo(s)" % positivo)
print("%i valor(es) negativo(s)" % negativo)