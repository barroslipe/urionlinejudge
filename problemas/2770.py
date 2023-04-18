import itertools
import sys

while True:
    try:
        x, y, m = map(int, input().split())
    except EOFError:
        exit(0)
    
    for _ in itertools.repeat(None, m):
        xi, yi = map(int, input().split())
        
        sys.stdout.write('Sim\n' if x >= xi and y >= yi or x >= yi and y >= xi else 'Nao\n')