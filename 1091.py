while True:
    k = int(input())

    if k == 0:
        exit()
    
    n, m = map(int, input().split())

    for c in range(k):
        x, y = map(int, input().split())
    
        if x == n or y == m:
            print('divisa')
        elif x > n:
            if y > m:
                print('NE')
            else:
                print('SE')
        else:
            if y < m:
                print('SO')
            else:
                print('NO')