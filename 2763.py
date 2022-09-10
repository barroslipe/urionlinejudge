cpf = input()

for i in cpf:
    if i != '.' and i != '-':
        print(i, end="")
    else:
        print()
print()