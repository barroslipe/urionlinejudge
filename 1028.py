n = int(input())

def mdc_euclide(f1, f2):
    if f2 == 0:
        return f1
    else:
        return mdc_euclide(f2, f1%f2)

for i in range(0, n):
    f1, f2 = map(int, input().split())

    mdc = mdc_euclide(f1, f2)

    print(mdc)