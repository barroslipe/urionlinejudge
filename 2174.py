n = int(input())

total_pokemons = 151

capturados = set()

for i in range(n):
    capturados.add(input())

print(f'Falta(m) {total_pokemons - len(capturados)} pomekon(s).')