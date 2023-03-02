
dicionario = set()
while True:
    try:
        linha = input()
    except EOFError:
        break
    
    nova_linha = ''
    for i in range(len(linha)):
    
        if 'A' <= linha[i] <= 'Z' or 'a' <= linha[i] <= 'z':
            nova_linha += linha[i]
        else:
            nova_linha += ' '

    for i in nova_linha.split():
        dicionario.add(i.lower())


nova = list(dicionario)

print(*(sorted(nova)), sep='\n')
