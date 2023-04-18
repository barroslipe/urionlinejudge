
while True:
    try:
        m = float(input())

    except EOFError:
        exit(0)

    segundos = (m*6*60*60)/90

    hora = segundos//(60*60)
    minuto = (segundos%(60*60))//60
    segundo = segundos%(60)
    

    if m >= 0 and m < 90:
        print('Bom Dia!!')    
    elif m >=90 and m < 180:
        print('Boa Tarde!!')
    elif m >= 180 and m <270:
        print('Boa Noite!!')
    else:
        print('De Madrugada!!')
    
    hora += 6

    if hora >= 24:
        hora -= 24
    
    print(f"{hora:02.0f}:{minuto:02.0f}:{segundo:02.0f}")
