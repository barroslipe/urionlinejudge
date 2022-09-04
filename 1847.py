a, b, c = map(int, input().split())

##desceu
if a > b:
    if b <= c:
        print(':)')
    else:
        if b - c < a - b:
            print(':)')
        else:
            print(':(')
#subiu
elif a < b:
    if b < c and b - a <= c - b:
        print(':)')
    else:
        print(':(')
#constante
else:
    if b < c:
        print(':)')
    else:
        print(':(')