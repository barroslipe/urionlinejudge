while True:
    n = int(input())

    if  n == 0:
        exit()
    
    presentes = list(map(int, input().split()))
    count_presentes = 2*n

    maior_par = menor_par = 0

    for i in range(0, count_presentes, 2):
        par = presentes[i] + presentes[count_presentes - 1 - i]

        if par > maior_par:
            maior_par = par
        
        if par < menor_par or i == 0:
            menor_par = par

    print(maior_par, menor_par)