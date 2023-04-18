c = int(input())
t = input()

soma = 0
step = c

for i in range(144):
    x = float(input())

    if i == step:
        soma += x
        step += 12

    if i > step or step > 143:
        print(f"{(soma if t == 'S' else soma/12):.1f}")
        break