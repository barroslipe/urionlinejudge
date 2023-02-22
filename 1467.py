while True:
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        exit(0)
    
    if a == b == c:
        print('*')
    elif a == b != c:
        print('C')
    elif b == c != a:
        print('A')
    else:
        print('B')