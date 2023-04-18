n =  int(input())

for i in range(n):
    palavras = input().split()

    tam = len(palavras)
    
    for j in range(tam):
        for k in range(tam-1):
            if len(palavras[k]) < len(palavras[k + 1]):
                palavras[k], palavras[k+1] = palavras[k+1], palavras[k]
    
    print(*palavras)