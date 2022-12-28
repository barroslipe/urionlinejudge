n = int(input())

for i in range(n):
    a, b = input().split()
    
    tamA = len(a)
    tamB = len(b)

    indice = 0
    shift = True
    while True:

        if shift:
            if indice < tamA:
                print(a[indice], end='')
        else:
            if indice < tamB:
                print(b[indice], end='')
            
            indice += 1

            if indice >= tamB and indice >= tamA:
                break
    
        shift = not shift

    print()