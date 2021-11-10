def fibonacci(a):
    
    fib = {}
    for i in range(a + 1):
        if i == 0:
            fib[i] = 0
        elif i == 1 or i == 2:
            fib[i] = 1
        else:
            fib[i]  = fib[i - 1] + fib[i - 2]
    
    return fib[a]

t = int(input())

for i in range(t):
    n = int(input())
    valor_fib = fibonacci(n)
    print(f"Fib({n}) = {valor_fib}")