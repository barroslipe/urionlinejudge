while True:
    try:
        sentenca = input()
    except EOFError:
        exit(0)
    
    up = True
    for i in sentenca:
        if i != ' ':
            print(i.upper() if up else i.lower(), end='')
            up = not up
        else:
            print(' ', end='')

    print()