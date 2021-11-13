n = int(input())

for i in range(n):
    mina = list(input())
    
    metade_direita = 0
    diamantes = 0
    while mina:
        escavada = mina.pop()

        if escavada == '>':
            metade_direita += 1
        elif escavada == '<'and metade_direita > 0:
            diamantes += 1
            metade_direita -= 1
    
    print(diamantes)