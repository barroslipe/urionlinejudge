while True:
    n = int(input())

    if n == 0:
        exit(0)
    
    tempos = list(map(int, input().split()))

    tempo = 10
    if len(tempos) > 1:
        for i in range(1, len(tempos)):
            if abs(tempos[i] - tempos[i-1]) > 10:
                tempo += 10
            else:
                tempo += abs(tempos[i] - tempos[i-1])
    print(tempo)