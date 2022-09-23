teste = 1
while True:
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        exit(0)
    
    n = int(input())

    meteoritos = 0
    for i in range(n):
        x, y = map(int, input().split())

        if x1 <= x <= x2 and y2 <= y <= y1:
            meteoritos += 1
    
    print('Teste', teste)
    print(meteoritos)

    teste += 1