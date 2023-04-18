CONSUMO_CARRO =  12

tempo =  int(input())
velocidade_media = int(input())

litros =  tempo * velocidade_media / CONSUMO_CARRO

print("%.3f" % litros)