n = int(input())

for i in range(n):
    linha = input()

    for l in linha[::-1]:
        if l.islower():
            print(l, end='')
    
    print()