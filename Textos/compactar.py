import os

lista = os.listdir(os.getcwd())
for f_name in lista:
    if f_name != 'compactar.py':
        f = open(f_name, 'r+', encoding='UTF-8')
        ordenado = sorted(set(f.readlines()))
        f.seek(0)
        f.truncate()
        for linea in ordenado:
            if linea != '\n':
                print(linea, end='', file=f)
        f.close()
