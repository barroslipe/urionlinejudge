n = int(input())

for i in range(n):
    x = int(input())
    print(f"{0 if x%2 == 0 else 1}")