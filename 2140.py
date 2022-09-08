
while True:
    
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        exit(0)
    
    notas = [2, 5, 10, 20, 50, 100]

    troco = m - n

    possivel = False
    for i in notas:
        for j in notas:
            if i + j == troco:
                possivel = True
                break
        if possivel:
            break
    
    if possivel:
        print('possible')
    else:
        print('impossible')