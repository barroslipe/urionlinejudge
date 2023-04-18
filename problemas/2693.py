while True:

    try:
    
        q = int(input())
    except EOFError:
        exit()

    alunos = []

    for i in range(q):
        nome, regiao, custo = input().split()

        alunos.append([nome, regiao, int(custo)])

    alunos.sort(key= lambda x: (x[2], x[1], x[0]))

    for el in alunos:
        print(el[0])