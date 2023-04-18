t = int(input())

for i in range(t):
    b = int(input())
    a, d, l = map(int, input().split())
    a2, d2, l2 = map(int, input().split())

    golpe = (a + d)/2 + (b if l%2==0 else 0)
    golpe2 = (a2 + d2)/2 + (b if l2%2==0 else 0)

    if golpe > golpe2:
        print('Dabriel')
    elif golpe < golpe2:
        print('Guarte')
    else:
        print('Empate')