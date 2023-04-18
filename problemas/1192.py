n = int(input())

for i in range(n):
    jogo = input()

    if jogo[0] == jogo[2]:
        print(int(jogo[0]) * int(jogo[2]))
    elif jogo[1].islower():
        print(int(jogo[0]) + int(jogo[2]))
    else:
        print(int(jogo[2]) - int(jogo[0]))