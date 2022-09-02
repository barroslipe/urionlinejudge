
def imprimir_par(par):
    for index, e in enumerate(par):
        print(f"par[{index}] = {e}")

def imprimir_impar(impar):
    for index, e in enumerate(impar):
        print(f"impar[{index}] = {e}")


par = []
impar = []

for i in range(15):
    x = int(input())

    if x%2 == 0:
        par.append(x)
        if len(par) == 5:
            imprimir_par(par)
            par = []

    else:
        impar.append(x)
        if len(impar) == 5:
            imprimir_impar(impar)
            impar = []

if len(impar) > 0:
    imprimir_impar(impar)
    impar = []

if len(par) > 0:
    imprimir_par(par)
    par = []