n = int(input())

while n != 0:

    a = list(map(int, input().split()))

    a.sort()
    sobrou = -1
    for i in range(0, n, 2):

        if i == (n - 1):
            sobrou = a[i]
        else:
            if a[i] != a[i + 1]:
                sobrou = a[i]
                break

    print(sobrou)

    n = int(input())