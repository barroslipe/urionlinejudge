while True:
    try:
        expressao = list(input())
    except EOFError:
        break

    abre_parenteses = 0
    while expressao:
        elemento = expressao.pop()

        if elemento == ')':
            abre_parenteses += 1
        elif elemento == '(':
            abre_parenteses -= 1
            if abre_parenteses < 0:
              break

    if abre_parenteses == 0:
        print("correct")
    else:
        print("incorrect") 