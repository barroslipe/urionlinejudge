while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    soma = 0
    for i in range(n):
        digito = m % 10
        soma += digito
        m = int(m/10)
        
    print(f"{soma} {'sim' if soma % 3 == 0 else 'nao'}")