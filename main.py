import os
import sys
import extractor
import conjugaciones
import time as t

# Se generan los archivos de texto necesarios 
# Se asume que como mínimo se cuenta con el
# archivo diccionario.txt (contenido crudo del diccionario de la RAE)
# y los archivos de verbos irregulares infinitivos y conjugados.
def inicializacion():
    print('Inicializando...')
    texts_path = os.getcwd() + os.sep + 'Textos'
    l_files = os.listdir(texts_path)
    if 'diccionario.txt' not in l_files:
        print('Falta archivo de diccionario.')
        exit()
    elif 'verbos_irregulares_infinitivos.txt' not in l_files:
        print('Falta archivo de verbos irregulares infinitivos.')
        exit()
    elif 'verbos_irregulares_conjugados.txt' not in l_files:
        print('Falta archivo de verbos irregulares conjugados.')
        exit()
    if 'palabras.txt' not in l_files or 'sus_adj.txt' not in l_files:
        extractor.extraer(texts_path)
    if ('verbos_regulares_infinitivos.txt' not in l_files) or ('verbos_regulares_conjugados.txt' not in l_files):
        conjugaciones.generar(texts_path)

if __name__ == '__main__':
    inicializacion()
    import herramientas
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