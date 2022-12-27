import math


while True:
    try:
        d, vf, vg = map(int, input().split())
    except EOFError:
        exit(0)

    hipotenusa = math.sqrt(12**2 + d**2)

    tempoG = hipotenusa / vg
    tempoF = 12 / vf

    if tempoG <= tempoF:
        print('S')
    else:
        print('N')