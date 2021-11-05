p = int(input())

cont = 0
velocidade = 0
distancia = 60000000

while cont < 10:

    primo = True

    for i in range(3, p):
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