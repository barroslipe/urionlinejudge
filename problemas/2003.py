while True:
    try:
        h, m = map(int, input().split(':'))
    except EOFError:
        exit(0)

    if h - 7 == 0:
        hf = 0
        mf = m
    elif h - 7 > 0:
        hf = h - 7
        mf = m
    else:
        hf = 0
        mf = 0
    
    print(f'Atraso maximo: {hf*60 + mf}')