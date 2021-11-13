while True:
    try:
        l = int(input())
    except EOFError:
        break
    
    lesmas = map(int, input().split())

    maior = max(lesmas)

    if maior < 10:
        print(1)
    elif maior >= 10 and maior < 20:
        print(2)
    else:
        print(3)