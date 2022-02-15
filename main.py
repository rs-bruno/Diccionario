import sys
import extraer_palabras
import conjugaciones

def inicializacion():
    print('Extrayendo palabras...')
    extraer_palabras.extraer('Textos\diccionario_rae_2014.txt')
    print('Generando conjugaciones...')
    conjugaciones.generar('Textos\palabras_extraidas.txt')

if __name__ == '__main__':
    inicializacion()
    inp = ''
    while not (inp == '1'):
        print('1) Salir.')
        print('Seleccione una opcion:')
        inp = input()
    match inp:
        case '1': exit()