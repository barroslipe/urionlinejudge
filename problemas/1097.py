i = 1
j = 7

while i < 10:
    for k in range(j, j-3, -1):
        print(f"I={i} J={k}")
    j += 2
    i += 2