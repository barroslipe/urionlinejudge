

fib = []

fib.append(0)
fib.append(1)
fib.append(2)

for i in range(3, 41):
    fib.append(fib[i-1] + fib[i-2])


while True:
    
    n = int(input())

    if n == 0:
        break


    print(fib[n])