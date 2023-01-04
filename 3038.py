dic = {'@': 'a', '&': 'e', '!': 'i', '*': 'o', '#': 'u'}
while True:
    try:
        frase = input()
    except EOFError:
        exit(0)
    
    for i in frase:
        if i in dic:
            print(dic[i], end='')
        else:
            print(i, end='')
    print()