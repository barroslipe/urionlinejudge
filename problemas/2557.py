import re

while True:
    try:
        expressao = input()
    except EOFError:
        exit(0)

    termos = re.split('[=+]', expressao)

    r = termos[0]
    l = termos[1]
    j = termos[2]

    if not r.isnumeric():
        print(int(j)-int(l))
    elif not l.isnumeric():
        print(int(j)-int(r))
    else:
        print(int(r)+int(l))