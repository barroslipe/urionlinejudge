n = int(input())

precos ={'1001': 1.5, '1002': 2.5, '1003': 3.5, '1004': 4.5, '1005': 5.5}
total = 0
for i in range(n):
    p, q = input().split()

    total += precos[p]*int(q)

print(f"{total:.2f}")