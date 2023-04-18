while True:
    try:
        tag_a = input()
        tag_b = input()

        texto = input()
    except EOFError:
        exit(0)
    
    print(texto.replace(tag_a, tag_b))