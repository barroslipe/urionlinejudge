
while True:
    n = int(input())

    if n == 0:
        exit(0)

    v_a = v_b = 0
    for i in range(n):
        a, b = map(int, input().split())

        if a > b:
            v_a += 1
        elif b > a:
            v_b += 1
    
    print(v_a, v_b)