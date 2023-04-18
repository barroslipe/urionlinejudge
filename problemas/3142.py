
alfabeto = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 
            'R': 18, 'S': 19 , 'T': 20, 'U': 21, 'V': 22, 'W': 23,'X': 24, 'Y': 25, 'Z': 26}

while True:
    try:
        celula = input()
    except EOFError:
        exit(0)
    
    tam = len(celula)
    
    if tam == 1:
        print(alfabeto[celula[0]])
    elif tam == 2:
        print( alfabeto[celula[0]]*26 + alfabeto[celula[1]] )
    elif tam == 3:
        valor = alfabeto[celula[0]]*676 + alfabeto[celula[1]]*26 + alfabeto[celula[2]]
        if valor <= 16384:
            print(valor)
        else:
            print('Essa coluna nao existe Tobias!')
    else:
        print('Essa coluna nao existe Tobias!')