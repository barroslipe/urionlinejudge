n = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(n)
for nota in cedulas:
    quantidade = int(n/nota)
    texto = "%i nota(s) de R$ %.2f" %(quantidade, nota)
    print(texto.replace('.', ','))
    n = n - quantidade * nota