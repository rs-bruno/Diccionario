import os
import sys
import conjugaciones
import time as t

def inicializacion():
    # Se conjugan los verbos regulares
    print('Inicializando...')
    texts_path = os.getcwd() + os.sep + 'Textos'
    l_files = os.listdir(texts_path)
    if 'palabras.txt' not in l_files:
        print('Falta archivo de palabras.')
        exit()
    elif 'verbos_irregulares_infinitivos.txt' not in l_files:
        print('Falta archivo de verbos irregulares infinitivos.')
        exit()
    elif 'verbos_irregulares_conjugados.txt' not in l_files:
        print('Falta archivo de verbos irregulares conjugados.')
        exit()
    elif ('verbos_regulares_infinitivos.txt' not in l_files) or ('verbos_regulares_conjugados.txt' not in l_files):
        conjugaciones.generar()

if __name__ == '__main__':
    inicializacion()
    import herramientas
    print()
    print('Lista de opciones')
    inp = ''
    while not (inp == '1' or inp == '2'):
        print('1) Porcentuar.')
        print('2) Salir.')
        print('Seleccione una opcion: ', end='')
        inp = input()
    if inp == '1':
        x = input('Ingrese un archivo: ')
        a = t.process_time_ns()
        herramientas.porcentuar(x)
        b = t.process_time_ns()
        print(f'Porcentuado en: {(b-a)/1000**2}ms')
    else:
        exit()