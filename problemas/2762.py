n = input()
a = b = ''

segunda = False
zeroesquerda = True
for i in n:
    if i == '.':
        segunda = True
        continue

    if segunda:

        if i == '0' and zeroesquerda:
            continue
        b += i
        zeroesquerda = False
    else:
        a += i

print(b + '.' + a)