n = int(input())

inicio_alfabeto = ord('A')
fim_alfabeto = ord('Z')

for i in range(n):
    codigo = list(input())
    chave = int(input())

    for j in range(len(codigo)):
        caracter_decodificado = ord(codigo[j]) - chave
        if caracter_decodificado < inicio_alfabeto:
            caracter_decodificado = fim_alfabeto - (inicio_alfabeto - caracter_decodificado) + 1

        codigo[j] = chr(caracter_decodificado)
        
    print(''.join(codigo))