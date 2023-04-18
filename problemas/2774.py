from math import sqrt


while True:
    try:
        h, m = map(int, input().split())
    except EOFError:
        exit(0)


    medidas = list(map(float, input().split()))

    somatorio = 0
    media = sum(medidas)/len(medidas)
    for i in medidas:
        somatorio += (i - media)**2

    print(f"{sqrt(somatorio / (len(medidas) -1)):.5f}")