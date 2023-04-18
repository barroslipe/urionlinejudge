while True:
    n = int(input())

    if n == 0:
        exit(0)
    
    jogos = input().split()

    mary = 0
    for j in jogos:
        if j == '0':
            mary += 1

    print("Mary won", mary, "times and John won", n - mary, "times")