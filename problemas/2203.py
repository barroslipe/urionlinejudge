
from math import sqrt


while True:
    try:
        x_f, y_f, x_i, y_i, v_i, rcu, rc = map(int, input().split())
    except EOFError:
        exit(0)

    distancia_f_i = sqrt((x_f - x_i)**2 +(y_f - y_i)**2)
    
    if distancia_f_i + 1.5*v_i <= rcu + rc:
        print('Y') 
    else:
        print('N')