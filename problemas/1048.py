salario = float(input())

if salario >= 0 and salario <= 400:
    porcentagem = 15
elif salario >= 400.01 and salario <= 800:
    porcentagem = 12
elif salario >= 800.01 and salario <= 1200:
    porcentagem = 10
elif salario >= 1200.01 and salario <= 2000:
    porcentagem = 7
else:
    porcentagem = 4

novo_salario = salario * (1 + porcentagem/100)
reajuste = novo_salario - salario

print("Novo salario: %.2f" % novo_salario)
print("Reajuste ganho: %.2f" % reajuste)
print("Em percentual: %i %%" % porcentagem)