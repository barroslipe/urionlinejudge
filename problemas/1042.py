a, b, c = map(int, input().split())

d, e, f = a, b, c

if a > c:
    a, c = c, a

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

print("%i\n%i\n%i\n" % (a, b, c))

print("%i\n%i\n%i" % (d, e, f))