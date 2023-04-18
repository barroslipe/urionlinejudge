a, b, c = map(float, input().split())

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

else:
    if (a * a) == (b * b + c * c):
        print("TRIANGULO RETANGULO")

    if (a * a) > (b * b + c * c):
        print("TRIANGULO OBTUSANGULO")

    if (a * a) < (b * b + c * c):
        print("TRIANGULO ACUTANGULO")

    if (a == b) and (b == c):
        print("TRIANGULO EQUILATERO")

    if (a == b) != (b == c):
        print("TRIANGULO ISOSCELES")