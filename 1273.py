
first = True
while True:

    n = int(input())

    if n == 0:
        break

    if not first:
        print()
    else:
        first = False

    palavras = []
    maior = 0
    for i in range(n):
        palavra = input()

        if len(palavra) > maior:
            maior = len(palavra)

        palavras.append(palavra)
    
    for i in range(n):
        print(f'{palavras[i]:>{maior}}')