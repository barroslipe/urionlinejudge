while True:

    n = int(input())

    if n == 0:
        exit(0)

    posicao = 1
    toques =  0
    for i in range(n):
        entrada = input().split()
        
        if entrada[posicao] == '1':
            if posicao == 0 and entrada[0] == '1':
                if entrada[1] == '0':
                    toques += 1
                    posicao = 1
                else:
                    toques += 2
                    posicao = 2

            elif posicao == 1 and entrada[1] == '1':
                if entrada[2] == '0':
                    posicao = 2
                else:
                    posicao = 0
                toques += 1
            
            elif posicao == 2 and entrada[2] == '1':
                if entrada[1] == '0':
                    toques += 1
                    posicao = 1
                else:
                    toques += 2
                    posicao = 0

    print(toques)