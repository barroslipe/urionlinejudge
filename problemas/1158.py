n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    step = soma = 0
    
    if x%2 != 0:
        step = x
    else:
        step = x + 1

    for j in range(y):
        soma +=  step
        step += 2


    print(soma)