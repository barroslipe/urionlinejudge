VELOCIDADE_X = 60
VELOCIDADE_Y = 90

distancia = int(input())

tempo = distancia/(VELOCIDADE_Y -  VELOCIDADE_X)

print("%i minutos" % (tempo * 60))