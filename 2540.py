while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)
    
    votos = input().split()

    if votos.count('1') >= 2*n/3:
        print('impeachment')
    else:
        print('acusacao arquivada')