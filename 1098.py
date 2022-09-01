
from decimal import Decimal


i = 0
j = 1

while i <= 2:

    print(f"I={i} J={j}\nI={i} J={j+1}\nI={i} J={j+2}")

    i += Decimal('0.2')
    j += Decimal('0.2')

    if i == 1:
        i = 1
    elif i == 2:
        i = 2

    if j == 2:
        j = 2
    elif j == 3:
        j = 3
    elif j == 4:
        j = 4