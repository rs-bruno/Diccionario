import sys

def linea_candidata(line, prev_line):
    ''' Primer filtro para encontrar palabras del diccionario.

    Se eligen lineas que pueden ser el inicio de una definición, y por lo tanto contener a la palabra como
    sufijo.'''
    ret = False
    if prev_line[0] == '\n' and line != '\n':
        ret = True
    prev_line[0] = line
    return ret

def descartar_palabra(p):
    ''' Se usan criterios para descartar lineas que se sabe que no son definiciones o que son palabras repetidas.'''
    if p.count(' ') > 1 and p.count('1') == p.count('2') == 0 :
        return True
    if not p[0].isalpha() or not p[0].islower():
        return True
    return False

def femeninizar(pre, suff):
    if suff.endswith('a'):
        first_suff = suff[0]
        if first_suff == 'a':
            if pre[len(pre)-1] == 'o':
                pre = pre[:len(pre)-1] + 'a'
            else:
                pre + 'a'
        else: #busco la ultima ocurrencia de la primera letra del suffijo en el prefijo.
            ind = len(pre) - 1
            while ind > 0 and pre[ind] != first_suff:
                ind = ind - 1
            pre = pre[:ind] + suff
    else: #endswith('triz')
        pre = pre[:len(pre)-3] + suff
    return pre

def limpiar_lista(lista_palabras):
    '''Se eliminan los 1 y 2, se elimina lo que está despues de las comas, y se agregan las formas femeninas de los sustantivos.'''
    filtro1 = []
    for p1 in lista_palabras:
        one = p1.find('1')
        if one > 0:
            filtro1.append(p1.replace('1', ''))
        else:
            filtro1.append(p1)
    filtro2 = []
    for p2 in filtro1:
        two = p2.find('2')
        if two > 0:
            filtro2.append(p2.replace('2', ''))
        else:
            filtro2.append(p2)
    filtro_spaces = []
    for ps in filtro2:
        filtro_spaces.append(ps.replace(' ', ''))
    proc_commas = []
    for pc in filtro_spaces:
        if pc.count(',') > 0:
            aux_list = pc.split(',')
            if aux_list[1].endswith('a') or aux_list[1].endswith('triz'):
                fem = femeninizar(*aux_list)
                proc_commas.append(fem)
                proc_commas.append(aux_list[0])
            else:
                proc_commas.append(aux_list[0])
        else:
            proc_commas.append(pc)
    res = []
    for r in proc_commas:
        if r.isalpha():
            res.append(r)
    final_res = []
    for i in range(1, len(res)-1): #saca palabras "coladas"
        if (res[i])[0] == (res[i-1])[0] or (res[i])[0] == (res[i+1])[0]:
            final_res.append(res[i])
    final_res = sorted(set(final_res))
    return final_res

def extraer(path):
    '''Extrae las palabras del texto del diccionario.'''
    word_set = ['0']
    prev_line = ['x']
    f = open(path, 'r+', encoding='UTF-8')
    for l in f:
        if linea_candidata(l, prev_line):
            dot = l.find('.')
            if (dot > 0) and not descartar_palabra(l[:dot]):
                word_set.append(l[:dot])
    f.close()
    lista_limpia = limpiar_lista(word_set)
    s = open('Textos/palabras_extraidas.txt', 'w+', encoding='UTF-8')
    for w in lista_limpia:
        s.write(w + '\n')
    s.close()
    print(f'Se extrajeron {len(lista_limpia)} palabras.')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extraer(sys.argv[1])