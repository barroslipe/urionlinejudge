
from math import floor


while True:

    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        exit(0)
    
    print(floor((a*b*c)**(1/3)))