while True:
    try:
        entrada = input()
    except EOFError:
        exit(0)
    
    processada = ''
    error = False
    for i in entrada:
        if i.lower() == 'o':
            processada += '0'
        elif i == 'l':
            processada += '1'
        elif i == ' ' or i == ',':
            continue
        elif not i.isdecimal() or i == '-' or (i == '+' and len(processada) > 0):
            error = True
            break
        else:
            processada += i
        
    if error or processada == '' or int(processada) > 2147483647 or int(processada) < 0:
        print('error')
    else:
        print(int(processada))