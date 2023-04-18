
while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    for l in range(n):
        for c in range(n):

            if l == (n//2) and c == (n//2):
                print(4, end='')
            elif n//3 <= l <= (n//2 + (n//2 - n//3)) and n//3 <= c <= (n//2 + (n//2 - n//3)):
                print(1, end='')
            elif l == c:
                print(2, end='')
            elif l + c == n-1:
                print(3, end='')
            else:
                print(0, end='')
        print()

    print()