from math import sqrt


def eh_primo(numero):
    if numero == 1:
        return False

    if numero == 2:
        return True

    if numero%2 == 0:
        return False

    eh_primo = True
    for i in range(3, int(sqrt(numero))+1, 2):
        if numero%i == 0:
            eh_primo = False
            break
    
    return eh_primo

while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)
    
    moedas = []
    for i in range(n):
        moedas.append(int(input()))
    
    salto = int(input())

    soma = 0
    for i in range(n-1, -1, -salto):
        soma += moedas[i]
    
    if eh_primo(soma):
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
    else:
        print('Bad boy! I’ll hit you.')