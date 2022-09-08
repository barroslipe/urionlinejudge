
from math import log


while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    print(f"{log(n, 2):.0f}")