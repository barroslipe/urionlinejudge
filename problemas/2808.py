o, d = input().split()

possibilidades = [
    chr(ord(o[0]) + 1) + str(int(o[1])+2),
    chr(ord(o[0]) + 2) + str(int(o[1])+1),
    chr(ord(o[0]) + 2) + str(int(o[1])-1),
    chr(ord(o[0]) + 1) + str(int(o[1])-2),
    chr(ord(o[0]) - 1) + str(int(o[1])+2),
    chr(ord(o[0]) - 2) + str(int(o[1])+1),
    chr(ord(o[0]) - 2) + str(int(o[1])-1),
    chr(ord(o[0]) - 1) + str(int(o[1])-2),
]

if d[0] >= 'a' and d[0] <= 'h' and d[1] >= '1' and d[1] <= '8' and d in possibilidades:
    print('VALIDO')
else:
    print('INVALIDO')