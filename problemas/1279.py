
primeiro_caso = True
while True:
    try:
        ano = int(input())
    except EOFError:
        exit(0)

    if not primeiro_caso:
        print()
    else:
        primeiro_caso = False
        
    festival = False
    if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
        festival = True
        print('This is leap year.')
    if ano%15 == 0:
        festival = True
        print('This is huluculu festival year.')
    if ano%55 == 0 and ((ano%4 == 0 and ano%100 != 0) or ano%400 == 0):
        festival = True
        print('This is bulukulu festival year.')

    if not festival:
        print('This is an ordinary year.')