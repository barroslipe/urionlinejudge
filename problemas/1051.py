salario = float(input())

if salario >= 0 and salario <= 2000:
    print("Isento")
else:
    valor_ir = 0

    if salario > 4500:
        valor_ir += (salario - 4500) * 0.28
        salario = 4500
    
    if salario >= 3000.01 and salario <= 4500:
        valor_ir += (salario - 3000.01) * 0.18
        salario = 3000
    
    if salario >= 2000.01 and salario <= 3000:
        valor_ir += (salario - 2000.01) * 0.08
        salario = 2000
    
    print("R$ %.2f" % (valor_ir))