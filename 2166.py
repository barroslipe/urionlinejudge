n = int(input())

denominador = 1/2
for i in range(1, n):
    denominador = 1/(2 + denominador)

if n == 0:
    print(f"{1:.10f}")
else:
    print(f"{1 + denominador:.10f}")