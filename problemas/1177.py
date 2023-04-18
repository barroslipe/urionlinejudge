t = int(input())
j = 0

for i in range(1000):
    print(f"N[{i}] = {j}")
    j += 1

    if j == t:
        j = 0