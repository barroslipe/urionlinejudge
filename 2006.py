t = input()
respostas = input().split()

acertos = 0
for i in respostas:
    if i == t:
        acertos += 1
print(acertos)