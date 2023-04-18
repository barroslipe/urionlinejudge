n = int(input())

fib = {}
fib[0] = 0

for i in range(1, n + 1):
    if i == 1:
        fib[i] = 0
    elif i == 2:
        fib[i] = 1
    else:
        fib[i] = fib[i - 1] + fib[i - 2]
    
    print(f"{fib[i]}", end="")
    if i != n:
        print(" ", end="")

print()