def is_triangulo(a, b, c):
    condicao_1 = (a < b + c) and (a > abs(b - c))
    condicao_2 = (b < a + c) and (b > abs(a - c))
    condicao_3 = (c < a + b) and (c > abs(a - b))

    return condicao_1 and condicao_2 and condicao_3

a, b, c = map(float, input().split())

if is_triangulo(a, b, c):
    print("Perimetro = %.1f" % (a + b + c))
else:
    print("Area = %.1f" % ((a + b) * c / 2))