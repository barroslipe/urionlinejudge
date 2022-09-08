achou = False
saida = ''
while True:

    try:
        l = input()
    except EOFError:
        exit(0)

    if l.find('</body>') > 0:
        print(saida, end="")
        exit(0)

    if achou:
        saida += l + '\n'

    if l.find('<body>') > 0:
        achou = True