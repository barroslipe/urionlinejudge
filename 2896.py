t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    cheias = (n)//k
    vazias = (n)%k
    print(cheias + vazias)