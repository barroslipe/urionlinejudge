
notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while True:

    n = input()

    if n == '*':
        exit()

    compassos = n.split('/')

    corretos = 0
    for compasso in compassos[1:-1]:
        total = 0
        for l in compasso:
            total += notas[l]
        
        if total == 1:
            corretos += 1
    
    print(corretos)