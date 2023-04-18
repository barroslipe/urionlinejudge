while True:
    try:
        n = int(input())
    except EOFError:
        break

    tamanho_arvore = int(n/2) + 1
    for i in range(tamanho_arvore):
        galho = ''
        for j in range(0, i * 2 + 1):
            galho += '*'
        print(f"{galho: >{tamanho_arvore + i}}")

    print(f"{'*':>{tamanho_arvore}}")
    print(f"{'***':>{tamanho_arvore + 1}}")
    print()