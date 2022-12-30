while True:
    try:
        num = float(input())
        cutoff = float(input())
    except EOFError:
        exit(0)

    num_int = int(num)
    if num_int != 0:
        parte_fracionada = num%num_int
    else:
        parte_fracionada = num

    if parte_fracionada > cutoff:
        print(num_int + 1)
    else:
        print(num_int)