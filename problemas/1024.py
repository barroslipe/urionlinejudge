n = int(input())

for i in range(n):
    texto = list(input())

    tam = len(texto)
    
    for l in range(tam//2):
        if 'a' <= texto[l] <= 'z' or 'A' <= texto[l] <= 'Z':
            texto[l] = chr(ord(texto[l]) + 3)
        
        if 'a' <= texto[tam - l - 1] <= 'z' or 'A' <= texto[tam - l - 1] <= 'Z':
            texto[tam - l - 1] = chr(ord(texto[tam - l - 1]) + 3)

        texto[l] = chr(ord(texto[l]) - 1)

        texto[l], texto[tam - l - 1] = texto[tam - l - 1], texto[l]
    
    if tam%2 != 0:
        if 'a' <= texto[tam//2] <= 'z' or 'A' <= texto[tam//2] <= 'Z':
            texto[tam//2] = chr(ord(texto[tam//2]) + 3)
        texto[tam//2] = chr(ord(texto[tam//2]) - 1)

    print(*texto, sep='')