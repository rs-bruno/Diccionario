import sys

def generar(path):
    '''Genera un archivo con las conjugaciones de todos los verbos encontrados en el archivo cuya ruta es *path*.'''
    verbos = []
    conjugaciones = []
    print(f'Se conjugaron {len(verbos)} verbos.')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generar(sys.argv[1])