n = int(input())

saques = saquet= bloqueios = bloqueiot = ataques = ataquet = 0


for i in range(n):
    nome = input()
    s, b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())

    saques += s1
    bloqueios += b1
    ataques += a1

    saquet += s
    bloqueiot += b
    ataquet += a

print(f"Pontos de Saque: {100*saques/saquet:.2f} %.")
print(f"Pontos de Bloqueio: {100*bloqueios/bloqueiot:.2f} %.")
print(f"Pontos de Ataque: {100*ataques/ataquet:.2f} %.")