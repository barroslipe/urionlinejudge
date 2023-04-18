while True:
    try:
        h, m = map(int, input().split())
    except EOFError:
        break

    hora_graus = 360/12
    hora = h/hora_graus

    minuto_graus = 360/60
    minuto = m/minuto_graus

    print(f"{hora:02.0f}:{minuto:02.0f}")