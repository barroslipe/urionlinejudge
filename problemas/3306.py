def mdc_euclides(a, b):
    while b != 0:        
        aux = b
        b = a % b
        a = aux

    return a

n, q = map(int, input().split())
conjunto = list(map(int, input().split()))

for i in range(q):
    queries = list(map(int, input().split()))

    if queries:
        if queries[0] == 1:
            for j in range(queries[1] - 1, queries[2]):
                conjunto[j] += queries[3]
        else:
            mdc = conjunto[queries[1] - 1]
            for k in range(queries[1] - 1, queries[2]):
                mdc = mdc_euclides(mdc, conjunto[k])
            print(mdc)
    else:
        print(i+1)