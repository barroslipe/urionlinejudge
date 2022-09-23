while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)
    
    seculo = n//100

    print(seculo+1 if n%100 > 0 else seculo)