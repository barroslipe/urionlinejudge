n = int(input())

for i in range(n):
    comida = float(input())
    dias = 0

    while comida > 1:
        comida = comida/2
        dias += 1
    
    print(dias, 'dias')