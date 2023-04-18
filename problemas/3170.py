b = int(input())
g = int(input())

if g%2 != 0:
    g -= 1

quantidade = g / 2 - b

if quantidade <= 0:
    print('Amelia tem todas bolinhas!')
else:
    print(f"Faltam {int(quantidade)} bolinha(s)")