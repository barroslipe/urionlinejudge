import math

p = int(input())

cont = 0
velocidade = 0
distancia = 60000000

while cont < 10:

    primo = True

    if p%2 == 0:
        primo = False
        p += 1
    else:
        for i in range(3, int(math.sqrt(p)) + 1, 2):
            if(p%i == 0):
                primo = False
                p += 1
                break

    if primo :
        cont += 1
        velocidade += p
        p += 1

print("%i km/h" % velocidade)

tempo = distancia / velocidade
dias = tempo / 24

print("%i h / %i d" % (tempo, dias))