n =  int(input())
a, b = map(int, input().split())

if n - a - b >= 0:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')