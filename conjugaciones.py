irregulares = open(r'Textos\verbos_irregulares_infinitivos.txt', 'r', encoding='UTF-8')
verbos_irregulares = {x for x in irregulares}
irregulares.close()

def extraer_infinitivos(path):
    '''Extrae verbos regulares.'''
    ret = []
    f = open(path, 'r+', encoding='UTF-8')
    for p in f:
        if p.endswith('ar\n') or p.endswith('er\n') or p.endswith('ir\n'):
            if p not in verbos_irregulares:
                ret.append(p.strip())
    return ret

def conjugar(verbo):
    '''Conjuga un verbo infinitivo.'''
    pass

def conjugar_verbos(lista_infinitivos):
    '''Conjuga una lista de verbos infinitivos regulares.'''
    ret = []
    for v in lista_infinitivos:
        aux = conjugar(v)
        if(aux != None):
            ret.extend(aux)
    return ret

def generar():
    '''Genera un archivo con las conjugaciones de todos los verbos encontrados en el archivo cuya ruta es *path*.'''
    print('Generando conjugaciones...')
    print('Extrayendo infinitivos regulares...')
    verbos = extraer_infinitivos(r'Textos\palabras.txt')
    f = open(r'Textos\verbos_regulares_infinitivos.txt', 'w+', encoding='UTF-8')
    print('Guardando archivo de infinitivos regulares...')
    for v in verbos:
        print(v, file=f)
    f.close()
    print('Conjugando infinitivos regulares...')
    conjugaciones = conjugar_verbos(verbos)
    f = open(r'Textos\verbos_regulares_conjugados.txt', 'w+', encoding='UTF-8')
    print('Guardando archivo de regulares conjugados...')
    for c in conjugaciones:
        print(c, file=f)
    f.close()
    print(f'Se conjugaron {len(verbos)} verbos.')
    print(f'Se generaron {len(conjugaciones)} formas conjugadas.')