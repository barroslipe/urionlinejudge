n = int(input())

incricao = maior_nota = 0
for i in range(n):
    mat, nota = map(str, input().split())

    if float(nota) > maior_nota:
        maior_nota = float(nota)
        incricao = mat

print(f"{incricao if maior_nota >= 8 else 'Minimum note not reached'}")