t = int(input())

for i in range(t):
    a, b = input().split()

    dif = 0
    for j in range(len(a)):
        dif += (ord(b[j]) - ord(a[j]))%26
    
    print(dif)