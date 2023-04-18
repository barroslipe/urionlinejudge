def diglet(i_buraco_origem, buracos):
    if buracos[i_buraco_origem] == -99:
        return 0
    else:
        i_buraco_destino = buracos[i_buraco_origem] - 1
        buracos[i_buraco_origem] = -99
        return 1 + diglet(i_buraco_destino, buracos)

def mdc_euclide(a, b):
    if b == 0:
        return a
    else:
        return mdc_euclide(b, a % b)

n = int(input())
buracos = list(map(int, input().split()))
caminhos = []

for i in range(0, n):
    ciclo = diglet(i, buracos)
    if ciclo != 0:
        caminhos.append(ciclo)

mmc = caminhos[0]
for j in range(0, len(caminhos) - 1):
    mmc = mmc * caminhos[j+1] / mdc_euclide(mmc, caminhos[j+1])

print("%i" % mmc)