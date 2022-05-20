# --------- Práctica dirigida Nro 2 - Módulo I Python ---------
# Alexander Burgos Ninatanta

# Problema 03

from funcionalidades_reloj import *


def hora_retrasada():
    return '{}:{}:{}'.format(hora_actual()+1, minuto_actual(), segundo_actual())


def fecha_actual():
    return '{}/{}/{}'.format(dia_actual(), mes_actual(), año_actual())

while True:
    print('Este programa puede mostrar:')

    ent = input("""
        1. Fecha actual
        2. Hora actual
        
        ¿Qué desea saber? Introduzca el número correspondiente:
        """)

    if ent == '1':
        print('Hora actual:', hora_retrasada())
        break
    elif ent == '2':
        print('Fecha actual:', fecha_actual())
        break
    else:
        print('Número ingresado fuera de rango. Introduzca nuevamente')