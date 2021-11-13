t = int(input())

for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())

    anos = 1
    while anos <= 100:
        pa = int(pa * (g1 + 100) / 100)
        pb = int(pb * (g2 + 100) / 100)

        if pa > pb:
            print(f"{anos} anos.")
            break

        anos += 1
    
    if anos > 100:
        print("Mais de 1 seculo.")