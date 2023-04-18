n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        print(j, end='')
    
    for k in range(b, a-1, -1):
        print(str(k)[::-1], end='')
    
    print()