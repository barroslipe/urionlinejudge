n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    print(f"{x*y//2} cm2")