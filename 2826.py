palavra1 = input()
palavra2 = input()

tam1 = len(palavra1)
tam2 = len(palavra2)

menor = 0

if tam1 < tam2:
    menor = tam1
else:
    menor = tam2

i = 0
while True:

    if i == menor:
        if tam1 < tam2:
            print(palavra1)
            print(palavra2)
        else:
            print(palavra2)
            print(palavra1)

        break
    elif palavra1[i] == palavra2[i]:
        i += 1
        continue
    elif palavra1[i] < palavra2[i]:
        print(palavra1)
        print(palavra2)
        break
    else:
        print(palavra2)
        print(palavra1)
        break