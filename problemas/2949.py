n = int(input())

hobbit = humano = elfo = anao = mago = 0
for i in range(n):
  nome, tipo = input().split()

  if tipo == 'A':
    anao += 1
  elif tipo == 'E':
    elfo += 1
  elif tipo == 'H':
    humano += 1
  elif tipo == 'M':
    mago += 1
  elif tipo == 'X':
    hobbit += 1

print(f"{hobbit} Hobbit(s)\n"
      f"{humano} Humano(s)\n"
      f"{elfo} Elfo(s)\n"
      f"{anao} Anao(oes)\n"
      f"{mago} Mago(s)")