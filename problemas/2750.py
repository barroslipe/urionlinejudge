for i in range(39):
    print('-', end="")
print()

print(f"{'|'}{'decimal':>9}{'|':>3}{'octal':>7}{'|':>3}{'Hexadecimal':>13}{'|':>3}")

for i in range(39):
    print('-', end="")
print()

for i in range(16):
    print(f"{'|'}{i:>7}{'|':>5}{i:>5o}{'|':>5}{i:>8X}{'|':>8}")


for i in range(39):
    print('-', end="")
print()