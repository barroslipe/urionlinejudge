n = int(input())

perdeu = 0
for i in range(n):
    porta = input()

    if porta != '1':
        perdeu += 1

print(perdeu)