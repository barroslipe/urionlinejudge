n = int(input())

for i in range(n):
    h, m, o = map(int, input().split())

    print(f"{h:02}:{m:02} - A porta {'abriu' if o == 1 else 'fechou'}!")