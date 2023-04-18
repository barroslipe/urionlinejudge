n = int(input())

while n != 0:
    texto = {}
    max_linha = 0
    for i in range(n):
        texto[i] = " ".join(input().split())
        if max_linha < len(texto[i]):
            max_linha = len(texto[i])
    
    for i in range(n):
        print(f"{texto[i]: >{max_linha}}")

    n = int(input())

    if n != 0:
        print()