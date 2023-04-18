
n = int(input())

denominador = 1/6
for i in range(1, n):
    denominador = 1/(6 + denominador)

if n == 0:
    print(f"{3:.10f}")
else:
    print(f"{3 + denominador:.10f}")