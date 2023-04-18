dia = hora = minuto = segundo = 0

dia_ini = int((input().split())[1])

segunda_entrada = input().split()
hor_ini = int(segunda_entrada[0])
min_ini = int(segunda_entrada[2])
seg_ini = int(segunda_entrada[4])

dia_fin = int((input().split())[1])

quarta_entrada = input().split()
hor_fin = int(quarta_entrada[0])
min_fin = int(quarta_entrada[2])
seg_fin = int(quarta_entrada[4])


if seg_fin >= seg_ini:
    segundo = seg_fin - seg_ini
else:
    segundo = 60 + (seg_fin - seg_ini)
    if min_ini < 59:
        min_ini += 1
    else:
        min_ini = 0
        if hor_ini < 23:
            hor_ini += 1
        else:
            hor_ini = 0
            dia_ini += 1

if min_fin >= min_ini:
    minuto = min_fin - min_ini
else:
    minuto = 60 + (min_fin - min_ini)
    if hor_ini < 23:
        hor_ini += 1
    else:
        hor_ini = 0
        dia_ini += 1

if hor_fin >= hor_ini:
    hora = hor_fin - hor_ini
else:
    hora = 24 + (hor_fin - hor_ini)
    dia_ini += 1

dia = dia_fin - dia_ini


print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")