from decimal import Decimal

notas = []


while True:
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        notas.append(nota)

        if len(notas) == 2:
            print(f"media = {Decimal((notas[0]+notas[1])/2):.2f}")
            notas = []
            
            resposta = 0
            while resposta < 1 or resposta > 2:
                print("novo calculo (1-sim 2-nao)")
                resposta = int(input())

                if resposta == 1:
                    break
                elif resposta == 2:
                    exit(0)