import sys
import extraer_palabras
import conjugaciones
import utilidades

def inicializacion():
    # TODO: Hacer que esto se haga solo cuando es necesario
    print('Extrayendo palabras...')
    extraer_palabras.extraer(r'Textos\diccionario.txt')
    print('Generando conjugaciones...')
    conjugaciones.generar(r'Textos\palabras_extraidas.txt')
    # TODO: Combinar palabras extraidas en un único archivo

if __name__ == '__main__':
    inicializacion()
    inp = ''
    while not (inp == '1'):
        print('1) Salir.')
        print('Seleccione una opcion:')
        inp = input()
    match inp:
        case '1': exit()