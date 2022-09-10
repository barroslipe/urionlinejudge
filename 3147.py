e = list(map(int, input().split()))

bem = e[0] + e[1] + e[2] + e[5]
mal = e[3] + e[4]

if bem >= mal:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')