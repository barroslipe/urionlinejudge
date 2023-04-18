regras = {'tesoura': ['papel', 'lagarto'],
          'papel': ['pedra', 'spock'],
          'pedra': ['lagarto', 'tesoura'],
          'lagarto': ['spock', 'papel'],
          'spock': ['tesoura', 'pedra'],
          }

n = int(input())

for i in range(n):
    r, s = input().split()

    if r == s:
        print('empate')
    elif s in regras[r]:
        print('rajesh')
    else:
        print('sheldon')