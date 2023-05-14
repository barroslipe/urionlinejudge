
fat = []
fat.append(0)
fat.append(1)

for i in range(2, 6):
    fat.append(i*fat[i-1])



while True:

    n = input()

    if n == '0':
        break

    saida = 0
    for index, l in enumerate(n[::-1]):
        saida += fat[index+1]*int(l)
    
    print(saida)