while True:
    n = int(input())

    if n == 0:
        exit(0)

    saida_planeta = ''
    saida_ano = 0
    for i in range(n):
        planeta, ano, tempo = input().split()

        aux = int(ano) - int(tempo)
        if  aux < saida_ano or i == 0:
            saida_ano = aux
            saida_planeta = planeta
    
    print(saida_planeta)