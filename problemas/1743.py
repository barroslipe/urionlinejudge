p1 =  input().split()
p2 = input().split()

valido = True
for i in range(len(p1)):
    if p1[i] == p2[i]:
        valido = False

if valido:
    print('Y')
else:
    print('N')