
import math

def is_primo(n):
    primo = True

    if n == 0 or n == 1:
        primo = False
    elif n % 2 == 0 and n != 2:
        primo = False
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                primo = False

    return primo

while True:
    try:
        n = int(input())
    except EOFError:
        break

    primo = is_primo(n)

    if not primo:
        print("Nada")
    else:
        super_primo = True

        for i in str(n):
            if not is_primo(int(i)):
                super_primo = False
        
        if super_primo:
            print("Super")
        else:
            print("Primo")