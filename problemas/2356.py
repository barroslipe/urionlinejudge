while True:
    try:
        d = input()
        s = input()
    except EOFError:
        exit(0)
    
    if d.find(s) != -1:
        print('Resistente')
    else:
        print('Nao resistente')