cifras = []

for i in range(26):
    linha = []
    for j in range(26):
        letra = 97 + j + i 
        if letra > 122:
            letra = 96 + letra%122
        linha.append(chr(letra))
    cifras.append(linha)

k = input()
n = int(input())

for i in range(n):
    mensagem = input().split()

    index = 0
    for ii, el in enumerate(mensagem):
        for j, letra in enumerate(el):
                if j == 0 and letra in ('a', 'e', 'i','o', 'u'):
                    print(el, end='')
                    break
                else:
                    letra_chave = k[index%len(k)]
                    print( cifras[ord(letra_chave) - 97][ord(letra) - 97] , end='')     # o n
                    index += 1
        if ii != len(mensagem) - 1:
            print(' ', end='')
    print()