tabela = [4, 4.5, 5, 2, 1.50]

codigo, quantidade = map(int,  input().split())

total = tabela[codigo - 1] * quantidade

print("Total: R$ %.2f" % total) 