m = int(input())

a = int(input())
b = int(input())

c = m - a - b
maior = 0

if a > b:
    if a > c:
        maior = a
    else:
        maior = c
elif b > c:
    maior = b
else:
    maior = c

print(maior)