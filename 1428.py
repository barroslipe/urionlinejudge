t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    w = (m-2)//3
    if (m-2)%3 > 0:
        w += 1
    
    h = (n-2)//3
    if (n-2)%3 > 0:
        h +=1

    print(w*h)