soma = step = 0

x = int(input())

while x != 0:

    if x%2 == 0:
        step = x
    else:
        step = x + 1
        
    for i in range(5):
        soma += step
        step += 2

    print(soma)
    soma = 0

    x = int(input())