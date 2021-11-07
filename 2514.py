
def mdc_euclide(a, b):
    if b == 0:
        return a
    else:
        return mdc_euclide(b, a%b)

while True:
    try:
        m = int(input())
        l1, l2, l3 = map(int, input().split())
    except EOFError:
        break


    if l1 > l2:
        l1, l2 = l2, l1
    if l2 > l3:
        l2, l3 = l3, l2
    if l1 > l2:
        l1, l2 = l2, l1 

    mdc_intermediario = mdc_euclide(l3, l2)
    mmc_intermediario = (l3 * l2) / mdc_intermediario

    mmc_total = (mmc_intermediario * l1 )/mdc_euclide(mmc_intermediario, l1)

    x = mmc_total - m

    print("%i" % x)