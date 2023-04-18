joias = []

while True:
    try:
        joia = input()

        if joias.count(joia) == 0:
            joias.append(joia)


    except EOFError:
        print(len(joias))
        exit(0)