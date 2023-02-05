m, n =  map(int, input().split())

cargos = {}
for i in range(m):
    cargo, salario = input().split()

    cargos[cargo] = int(salario)

for i in range(n):

    salario = 0
    while True:
        frase = input().split()

        if frase[0] == '.':
            break
    
        for f in frase:
            if f in cargos:
                salario += cargos[f]
        
    
    print(salario)