
while True:
    try:
        jogos = input().split()
    except EOFError:
        exit(0)
    
    vencedor = -1
    for i in range(3):
        if (jogos[i%3] == 'papel' and jogos[(i+1)%3] == 'pedra' and jogos[(i+2)%3] == 'pedra') or (jogos[(i)%3] == 'tesoura' and jogos[(i+1)%3] == 'papel' and jogos[(i+2)%3] == 'papel') or (jogos[(i)%3] == 'pedra' and jogos[(i+1)%3] == 'tesoura' and jogos[(i+2)%3] == 'tesoura'):
            vencedor = i
            break

    if vencedor == 0:
        print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
    elif vencedor == 1:
        print("Iron Maiden's gonna get you, no matter how far!")
    elif vencedor == 2:
        print('Urano perdeu algo muito precioso...')
    else:
        print('Putz vei, o Leo ta demorando muito pra jogar...')