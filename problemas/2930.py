e, d = map(int, input().split())

if e <= d - 3:
    print('Muito bem! Apresenta antes do Natal!')
elif e > d-3 and e <= d:
    print('Parece o trabalho do meu filho!')
    if e + 2 < 24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')

else:
    print('Eu odeio a professora!')