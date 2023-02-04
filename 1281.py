n = int(input())

for i in range(n):

    mercado = {}

    m = int(input())
    for j in range(m):
        fruta, preco = input().split()

        mercado[fruta] = float(preco)

    conta = 0

    p = int(input())
    for j in range(p):
        fruta, quantidade =  input().split()

        conta += mercado[fruta] * int(quantidade)
    
    print(f"R$ {conta:.2f}")