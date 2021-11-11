meu_ah = input()
medico_ah = input()

meu_contador_a = meu_ah.count('a')
medico_contador_a = medico_ah.count('a')

if meu_contador_a >= medico_contador_a:
    print("go")
else:
    print("no")