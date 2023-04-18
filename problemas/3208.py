from math import sqrt

while True:
    k, l = map(int, input().split())

    if k == 0 and l == 0:
        exit(0)
    
    a = 0
    if k%2 == 0:
        a = 2
    else:    
        for i in range(3, int(sqrt(k))+1, 2):

            if i < l:
                if k%i == 0:
                    a = i
                    break
            else:
                a = l + 1
                break

    if a < l:
        print('BAD', a)
    else:
        print('GOOD')