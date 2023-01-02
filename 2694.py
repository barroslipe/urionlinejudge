n = int(input())

for i in range(n):
    linha = input()

    soma = 0
    numero = ''
    for l in linha:
        if l.isdigit():
            numero += l
        else:
            if numero != '':
                soma += int(numero)
            numero = ''
    
    if numero != '':
        soma += int(numero)

    print(soma)