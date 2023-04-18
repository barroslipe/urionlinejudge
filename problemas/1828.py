t = int(input())

regras = {'tesoura': ['papel', 'lagarto'],
          'papel': ['pedra', 'Spock'],
          'pedra': ['lagarto', 'tesoura'],
          'lagarto': ['Spock', 'papel'],
          'Spock': ['tesoura', 'pedra'],
         }

for i in range(t):
    sheldon, raj = input().split()

    if sheldon == raj:
        print(f"Caso #{i+1}: De novo!")
    elif regras[sheldon].count(raj) > 0:
        print(f"Caso #{i+1}: Bazinga!")
    else:
        print(f"Caso #{i+1}: Raj trapaceou!")