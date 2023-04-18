renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

entrada = map(int, input().split())

bolas = sum(entrada)

print(renas[bolas%9 - 1])