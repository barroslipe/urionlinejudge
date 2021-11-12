def similar(palavra, palavra_dicionario):

    if len(palavra) != len(palavra_dicionario):
        return False
    else:
        
        diferenca = 0
        for i in range(len(palavra_dicionario)):
            if palavra[i] != palavra_dicionario[i]:
                diferenca += 1

        if diferenca <= 1:
            return True
        else:
            return False

n  = int(input())

dicionario =  ["one", "two", "three"]

for i in range(n):
    palavra = input()

    for j in range(3):
        if similar(palavra, dicionario[j]):
            print(j + 1)
            break