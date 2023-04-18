varetas = list(map(int, input().split()))

pode = False
for i in range(2):
    for j in range(i+1, 3):
        for k in range(j+1, 4):
            if varetas[i] + varetas[j] > varetas[k] and abs(varetas[i] - varetas[j]) < varetas[k]:
                pode = True

if pode:
    print('S')
else:
    print('N')