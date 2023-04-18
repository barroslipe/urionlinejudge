while True:
    try:
        n = int(input())
    except EOFError:
        exit(0)

    recorde = vm_anterior = 0

    for i in range(n):
        t, d = map(int, input().split())
        
        vm_atual = d/t
        
        if vm_atual > vm_anterior:
            vm_anterior = vm_atual
            print(i+1)