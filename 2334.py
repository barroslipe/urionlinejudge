while True:
    
    p = int(input())
    
    if p == -1:
        exit(0)

    print(f"{ p-1 if p -1 > 0 else 0}")