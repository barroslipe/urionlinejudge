while True:
    try:
        soma = 0
        n, min, max = map(int, input().split())

        
        for i in range(n):
            p = int(input())

            if p >= min and p <= max:
                soma +=1

        print(soma)
    except EOFError:
        exit(0)