while True:
    try:
        dolares = int(input())
        centavos = int(input())
    except EOFError:
        break

    print(f"${dolares:,}.{centavos:02d}")