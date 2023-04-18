while True:
    try:
        v = float(input())
        d = float(input())
    except EOFError:
        exit(0)

    area = 3.14*(d/2)*(d/2)
    altura = v/(3.14*(d/2)*(d/2))

    print(f"ALTURA = {altura:.2f}")
    print(f"AREA = {area:.2f}")