nome = input()
data_atual = input().split('/')
data_nascimento = input().split('/')

if data_atual[0] == data_nascimento[0] and data_atual[1] == data_nascimento[1]:
    print('Feliz aniversario!')

anos = int(data_atual[2]) - int(data_nascimento[2])
idade = anos

meses = int(data_atual[1]) - int(data_nascimento[1])
if meses < 0:
    idade = anos - 1
elif meses == 0:
    dias = int(data_atual[0]) - int(data_nascimento[0])
    if dias < 0:
        idade = anos - 1

print(f'Voce tem {idade} anos {nome}.')