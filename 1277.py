n = int(input())

for i in range(n):
    quantidade_alunos = int(input())

    alunos = input().split()
    frequencias = input().split()

    faltantes = []
    
    for index, frequencia in enumerate(frequencias):
        presente = 0
        total_aulas = 0
        for f in frequencia:
            if f == 'P':
                presente += 1
                total_aulas +=1
            elif f == 'A':
                total_aulas += 1


        if presente/total_aulas < 0.75:
            faltantes.append(alunos[index])

    print(*faltantes)