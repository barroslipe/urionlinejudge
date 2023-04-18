
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


n = int(input())

for i in range(n):
    expressao = input().split()

    n1 = int(expressao[0])
    d1 = int(expressao[2])
    op = expressao[3]
    n2 = int(expressao[4])
    d2 = int(expressao[6])

    if op == '+':
        num = n1*d2 + n2*d1
        den = d1*d2
    elif op == '-':
        num = n1*d2 - n2*d1
        den = d1*d2
    elif op == '/':
        num = n1*d2
        den = n2*d1
    else:
        num = n1*n2
        den = d1*d2

    divisor = mdc(num, den)

    print(str(num) + '/' + str(den) + ' = ' + str(num//divisor) + '/' + str(den//divisor))