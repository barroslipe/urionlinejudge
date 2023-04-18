while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    marcos = []
    leonardo = []

    m, l = map(int, input().split())

    for j in range(m):
        e1 = list(map(int, input().split()))
        marcos.append(e1)

    for j in range(l):
        e2 = list(map(int, input().split()))
        leonardo.append(e2)

    cm, cl = map(int, input().split())

    cartaMarcos = marcos[cm-1]
    cartaLeonardo = leonardo[cl-1]

    atributoSorteado = int(input())
    
    if cartaMarcos[atributoSorteado-1] > cartaLeonardo[atributoSorteado-1]:
        print('Marcos')
    elif cartaMarcos[atributoSorteado-1] < cartaLeonardo[atributoSorteado-1]:
        print('Leonardo')
    else:
        print('Empate')