while True:
    try:
        n, d = map(int, input().split())
    except EOFError:
        exit(0)
    
    data = ''
    for i in range(d):
        linha = input().split()

        pizza = True
        for j in linha[1:]:
            if j == '0':
                pizza = False
                break
        
        if pizza and data == '':
            data = linha[0]

    
    if data != '':
        print(data)
    else:
        print('Pizza antes de FdI')