a, b, c = map(float, input().split())

maior = (a + b + abs(a - b))/2

maior = (maior + c + abs(maior - c))/2

print("%i eh o maior" % maior)