
x = 0
inter_v = gremio_v = empate = 0

while x != 2:
    inter, gremio = map(int, input().split())

    if inter > gremio:
        inter_v += 1
    elif inter < gremio:
        gremio_v += 1
    else:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    x = int(input())

print( f"{inter_v+gremio_v+empate} grenais\n"
       f"Inter:{inter_v}\n"
       f"Gremio:{gremio_v}\n"
       f"Empates:{empate}")

if gremio_v > inter_v:
    print("Gremio venceu mais")
elif inter_v > gremio_v:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")