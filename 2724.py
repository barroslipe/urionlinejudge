n = int(input())

for i in range(n):
    
    compostos = []
  
    n_c = int(input())
    for j in range(n_c):
        compostos.append(input())
    
    n_e = int(input())
    for j in range(n_e):
        experiencia = input()

        perigoso = False
        for k in compostos:
            if experiencia.find(k) != -1:
                posicao = experiencia.find(k) + len(k)
                if not(posicao < len(experiencia) and (experiencia[posicao].isdigit() or experiencia[posicao].islower())):
                    perigoso = True
                    break
    
        if perigoso:
            print('Abortar')
        else:
            print('Prossiga')

    if i != n-1:
        print()