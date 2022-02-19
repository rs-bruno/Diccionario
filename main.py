import sys
import conjugaciones
import herramientas

def inicializacion():
    # Se conjugan los verbos regulares
    conjugaciones.generar()

if __name__ == '__main__':
    inicializacion()
    print('\n\n', end='')
    inp = ''
    while not (inp == '1'):
        print('1) Salir.')
        print('Seleccione una opcion: ', end='')
        inp = input()
    if inp == '1':
        exit()