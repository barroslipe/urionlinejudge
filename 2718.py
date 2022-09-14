n = int(input())

for i in range(n):
    x = int(input())

    binario = ''
    
    while x != 0:
        binario = str(x%2) + binario
        x = x//2
    
    seq = 0
    maior = 0
    for j in binario:
        if j == '1':
            seq += 1
        
        if seq > maior:
            maior = seq
        
        if j == '0':
            seq = 0


    if seq > maior:
        maior = seq
        
    print(maior)