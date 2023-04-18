from decimal import Decimal


soma  = 1

for i in range(2, 101):
    soma += Decimal(1/i)

print(f"{soma:.2f}")