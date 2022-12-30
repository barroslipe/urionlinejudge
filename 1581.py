n = int(input())

for i in range(n):
    k = int(input())

    idioma = input()
    for j in range(k-1):
        idioma_aux = input()

        if idioma != idioma_aux:
            idioma = 'ingles'

    print(idioma)