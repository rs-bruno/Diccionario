import sys

# TODO: Completar de extraer lista de verbos irregulares del libro
irregulares = open(r'Textos\verbos_irregulares_infinitivos.txt', 'r', encoding='UTF-8')
verbos_irregulares = {x for x in irregulares}
irregulares.close()

def extraer_verbos(path):
    '''Extrae verbos regulares.'''
    ret = []
    f = open(path, 'r+', encoding='UTF-8')
    for p in f:
        if p.endswith('ar\n') or p.endswith('er\n') or p.endswith('ir\n'):
            if p not in verbos_irregulares:
                ret.append(p.strip())
    return ret

def generar(path):
    '''Genera un archivo con las conjugaciones de todos los verbos encontrados en el archivo cuya ruta es *path*.'''
    verbos = extraer_verbos(r'Textos\palabras_extraidas.txt')
    # print(verbos)
    conjugaciones = []
    # TODO: Generar conjugaciones
    f = open(path, 'w+', encoding='UTF-8')
    f.writelines(conjugaciones)
    f.close()
    print(f'Se conjugaron {len(verbos)} verbos.')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generar(sys.argv[1])