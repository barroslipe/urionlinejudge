def mdc_euclide(a, b):
    if b == 0:
        return a
    else:
        return mdc_euclide(b, a%b)

while True:

    try:
        azuis, pretas, equipes = map(int, input().split())
    except EOFError:
        break

    mdc = mdc_euclide(azuis, pretas)

    if azuis/mdc + pretas/mdc >= equipes:
        print("sim")
    else:
        print("nao")