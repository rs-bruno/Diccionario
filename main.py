import sys
import palabras
import conjugaciones
import utilidades

def inicializacion():
    # TODO: Hacer que esto se haga solo cuando es necesario
    print('Extrayendo palabras...')
    palabras.extraer(r'Textos\diccionario.txt')
    print('Generando conjugaciones...')
    conjugaciones.generar()
    # TODO: Combinar palabras extraidas en un único archivo

if __name__ == '__main__':
    inicializacion()
    inp = ''
    while not (inp == '1'):
        print('1) Salir.')
        print('Seleccione una opcion: ', end='')
        inp = input()
    match inp:
        case '1': exit()