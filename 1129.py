alternativa = ['A', 'B', 'C', 'D', 'E']
while True:
    n = int(input())

    if n == 0:
        exit(0)

    for i in range(n):
        questoes = map(int, input().split())

        escolha = -1
        for index, el in enumerate(questoes):
            if el <= 127:
                if escolha != -1:
                    escolha = -1
                    break
                else:
                    escolha = index
        
        if escolha == -1:
            print('*')
        else:
            print(alternativa[escolha])