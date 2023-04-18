while True:

    try:
        m, d = map(int, input().split())
    except EOFError:
        exit(0)

    meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    fim = 0
    for i in meses:
        fim += i
    fim -= 6

    origem = 0
    for i in range(m):
        origem += meses[i]
    origem -= meses[m-1] - d


    if fim == origem:
        print('E natal!')
    elif origem == fim - 1:
        print('E vespera de natal!')
    elif origem > fim:
        print('Ja passou!')
    else:
        print(f"Faltam {fim - origem} dias para o natal!")