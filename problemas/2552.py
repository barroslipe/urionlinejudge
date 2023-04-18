from platform import java_ver


while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        exit(0)

    pao_queijo = []

    for i in range(n):
        pao_queijo.append(input().split())

    for i in range(n):
        for j in range(m):
            if pao_queijo[i][j] == '1':
                pao_queijo[i][j] = '9'
            else:
                ao_redor = 0

                if i-1 >= 0:
                    if pao_queijo[i-1][j] in ['1', '9']:
                        ao_redor += 1

                if i+1 < n:
                    if pao_queijo[i+1][j] in ['1', '9']:
                        ao_redor += 1
                   
                if j-1 >= 0:
                    if pao_queijo[i][j-1] in ['1', '9']:
                        ao_redor += 1

                if j+1 < m:
                    if pao_queijo[i][j+1] in ['1', '9']:
                        ao_redor += 1

                pao_queijo[i][j] = ao_redor
    
    for i in range(n):
        for j in range(m):
            print(pao_queijo[i][j], end="")
        print()