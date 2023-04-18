n = int(input())

while n> 0:
    if 900 <= n <= 999:
        print('CM', end="")
        n -= 900
    elif 500 <= n <= 899:
        print('D', end="")
        n -= 500
    elif 400 <= n <= 499:
        print('CD', end="")
        n -= 400
    elif 100 <= n <= 399:
        print('C', end="")
        n -= 100
    elif 90 <= n <= 99:
        print('XC', end="")
        n -= 90
    elif 50 <= n <= 89:
        print('L', end="")
        n -= 50
    elif 40 <= n <= 49:
        print('XL', end="")
        n -= 40
    elif 10 <= n <= 39:
        print('X', end="")
        n -= 10
    elif n == 9:
        print('IX', end="")
        n -= 9
    elif 5 <= n <= 8:
        print('V', end="")
        n -= 5
    elif n == 4:
        print('IV', end="")
        n -= 4
    else:
        print('I', end="")
        n -= 1
print()