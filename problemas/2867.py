c = int(input())

for i in range(c):
    n, m = map(int, input().split())
    print(len(str(n**m)))