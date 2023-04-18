n  = int(input())

acc_ida = acc_volta = 0
aux_ida = aux_volta = 0

anterior = ''

for i in range(n):
    ida, volta = input().split()

    if ida == 'chuva':
        if  aux_ida == 0:
            acc_ida += 1
            aux_volta += 1
        else:
            aux_volta += 1
            aux_ida -= 1

    if volta == 'chuva':
        if aux_volta == 0:
            acc_volta += 1
            aux_ida += 1
        else:
            aux_ida += 1
            aux_volta -= 1

    anterior = volta

print(acc_ida, acc_volta)