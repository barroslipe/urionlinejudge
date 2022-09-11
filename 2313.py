a, b, c = map(int, input().split())

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print('Valido-Equilatero')
    elif a != b and b != c and c != a:
        print('Valido-Escaleno')
    else:
        print('Valido-Isoceles')
    

    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
        print('Retangulo: S')
    else:
        print('Retangulo: N')

else:
    print('Invalido')