n1, n2, n3, n4 = map(float, input().split())

media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4) / 10

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print ("Aluno reprovado.")
else:
    print("Aluno em exame.")
    n_exame = float(input())

    print("Nota do exame: %.1f" % n_exame)

    nova_media = (media + n_exame) / 2

    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: %.1f" % nova_media)