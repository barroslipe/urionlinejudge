n = int(input())

for i in range(n):
    
    l = int(input())
    saida = 0
    for j in range(l):
        
        palavra = input()
        
        for index, i in enumerate(palavra):
            saida += (ord(i) - ord('A')) + j + index
        
    print(saida)