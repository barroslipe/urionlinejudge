def fmdc(a, b):
    if b == 0:
        return a
    else:
        return fmdc(b, a%b)

while True:
    try:
        x, y = map(int, input().split())
    except EOFError:
        exit(0)
    
    mdc = fmdc(x, y)

    estacas = (x*2 + y*2) // mdc

    print(estacas)