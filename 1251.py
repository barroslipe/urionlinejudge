first = True
while True:
    try:
        entrada = input()
    except EOFError:
        exit(0)

    if first:
        first = not first
    else:
        print() 

    frequencias =  {}

    for i in entrada:
        frequencias[ord(i)] = entrada.count(i)
    
    nova_lista = sorted(list(frequencias.items()), key= lambda x: (x[1], -x[0]))

    for i in nova_lista:
        print(i[0], i[1])