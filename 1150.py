x = int(input())
cont = 1

while True:
    z = int(input())

    if z > x:
        for i in range(x+1, int(z/2)):
            x += i
            cont += 1
            if x > z:
                print(cont)
                exit(0)