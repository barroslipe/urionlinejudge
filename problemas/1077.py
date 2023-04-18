
dic_operadores = {}
dic_operadores['^'] = 4
dic_operadores['*'] = 3
dic_operadores['/'] = 3
dic_operadores['+'] = 2
dic_operadores['-'] = 2
dic_operadores['('] = 1

n = int(input())

for i in range(n):
    expressao = input()
    operadores = []

    for l in expressao:
        if l in '+-*/^':
            while len(operadores) != 0 and dic_operadores[operadores[-1]] >= dic_operadores[l]:
                print(operadores.pop(), end='')
            operadores.append(l)
        elif l == '(':
            operadores.append(l)
        elif l == ')':
            i = operadores.pop()
            while i != '(':
                print(i, end='')
                i = operadores.pop()
        else:
            print(l, end='')
    
    while len(operadores) != 0:
         print(operadores.pop(), end='')

    print()