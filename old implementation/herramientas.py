#   Herramientas de manipulación del diccionario.
#   Éstas funciones asumen la existencia de los siguientes archivos:
#       Textos\verbos_irregulares_infinitivos.txt
#       Textos\verbos_irregulares_conugados.txt
#       Textos\palabras.txt
#       Textos\sus_adj.txt
#       Textos\verbos_regulares_infinitivos.txt
#       Textos\verbos_regulares_conjugados.txt
#   La funcionalidad del módulo depende de dichos archivos.
import os
import time as t

n_int = 1
def print_intervalo(a,b):
    global n_int
    '''Funcion auxiliar: imprime la cantidad de tiempo transcurrido entre dos instantes'''
    print(f'Intervalo {n_int} = {(b-a)/1000**2}ms')
    n_int = n_int + 1

#   Estructura auxiliar, conjunto de todas las palabras.
palabras_f = open(os.getcwd()+os.sep+'Textos'+os.sep+'palabras.txt', 'r', encoding='UTF-8')
palabras_set = {w[:len(w)-1] for w in palabras_f} #Se quitan los sufijos '\n'
palabras_f.close()

#   Estructura auxiliar, conjunto de conjugaciones de verbos irregulares,
#   se agregan a conjunto con todas las palabras, porque se considera a cada conjugación
#   de los verbos irregulares como palabras individuales, a diferencia de los verbos
#   regulares, para los cuales, el verbo y todas sus conjugaciones cuentan como una única
#   palabra.
irregulares_f = open(os.getcwd()+os.sep+'Textos'+os.sep+'verbos_irregulares_conjugados.txt', 'r', encoding='UTF-8')
irregulares_set = {w[:len(w)-1] for w in irregulares_f}
irregulares_f.close()
palabras_set = palabras_set | irregulares_set

regulares_f = open(os.getcwd()+os.sep+'Textos'+os.sep+'verbos_regulares_conjugados.txt', 'r', encoding='UTF-8')
regulares_list = [w[:len(w)-1] for w in regulares_f]
regulares_f.close()

sus_adj_f = open(os.getcwd()+os.sep+'Textos'+os.sep+'sus_adj.txt', 'r', encoding='UTF-8')
sus_adj_list = [w[:len(w)-1] for w in sus_adj_f]
sus_adj_f.close()

def noalpha_to_space(linea):
    buff = ''
    for caracter in linea:
        if not caracter.isalpha():
            buff = buff + ' '
        else:
            buff = buff + caracter
    return buff

def bin_search(str, list):
    inf = 0
    sup = len(list) - 1
    med = (sup + inf) // 2
    while (inf <= sup) and (str != list[med]):
        if str < list[med]:
            sup = med - 1
        else:
            inf = med + 1
        med = (sup + inf) // 2
    if str == list[med]:
        return True
    else:
        return False

def porcentuar(path):
    '''Calcula una estimación del porcentaje de la lengua española utilizada.'''
    # t1_i = t.process_time_ns() #
    f = open(path, 'r', encoding='UTF-8')
    lines_raw = f.readlines()
    f.close()
    # t1_f = t.process_time_ns() #
    # print_intervalo(t1_i, t1_f) #


    # t2_i = t.process_time_ns() #
    lines_clean = []
    for l_r in lines_raw:
        lines_clean.append(noalpha_to_space(l_r))
    # t2_f = t.process_time_ns() #
    # print_intervalo(t2_i, t2_f) #

    # t3_i = t.process_time_ns() #
    words = {'0'}
    words.remove('0')
    for l_c in lines_clean:
        aux = [w.lower() for w in l_c.split()]
        words.update(aux)
    # t3_f = t.process_time_ns() #
    # print_intervalo(t3_i, t3_f) #

    # t4_i = t.process_time_ns() #
    total = len(palabras_set)
    cant_presentes = 0
    for p in palabras_set:
        if p in words:
            cant_presentes = cant_presentes + 1
            words.remove(p)
    # t4_f = t.process_time_ns() #
    # print_intervalo(t4_i, t4_f) #

    # t5_i = t.process_time_ns() #
    bools_verbos_regulares = [False for x in range(len(regulares_list) // 53)]
    bools_sus_adj = [False for x in range(len(sus_adj_list) // 4)]
    # t5_f = t.process_time_ns() #
    # print_intervalo(t5_i, t5_f) #

    # t6_i = t.process_time_ns() #
    a_quitar = {'0'}
    a_quitar.remove('0')
    regulares_set_ordenado = sorted(list(zip(range(len(regulares_list)), regulares_list)), key=lambda x:x[1])
    sus_adj_set_ordenado = sorted(list(zip(range(len(sus_adj_list)), sus_adj_list)), key=lambda x:x[1])
    words_ordenado = sorted(words)
    i = 0
    j = 0
    for w in words_ordenado:
        if(i >= len(regulares_set_ordenado) and j >= len(sus_adj_set_ordenado)):
            break
        while i < len(regulares_set_ordenado) and w > regulares_set_ordenado[i][1]:
            i = i + 1
        if(i < len(regulares_set_ordenado) and w == regulares_set_ordenado[i][1]):
            a_quitar.add(regulares_set_ordenado[i][1])
            pos_lista = regulares_set_ordenado[i][0]
            if not bools_verbos_regulares[pos_lista // 53]:
              bools_verbos_regulares[pos_lista // 53] = True
              cant_presentes = cant_presentes + 1
        while j < len(sus_adj_set_ordenado) and w > sus_adj_set_ordenado[j][1]:
            j = j + 1
        if(j < len(sus_adj_set_ordenado) and w == sus_adj_set_ordenado[j][1]):
            pos_lista = sus_adj_set_ordenado[j][0]
            if not bools_sus_adj[pos_lista // 4]:
              a_quitar.add(sus_adj_set_ordenado[j][1])
              bools_sus_adj[pos_lista // 4] = True
              cant_presentes = cant_presentes + 1
    # t6_f = t.process_time_ns() #
    # print_intervalo(t6_i, t6_f) #

    # t8_i = t.process_time_ns() #
    words = words - a_quitar
    # t8_f = t.process_time_ns() #
    # print_intervalo(t8_i, t8_f) #

    # t7_i = t.process_time_ns() #
    tt = t.localtime()
    outputname = f'ausentes_{tt.tm_year}_{tt.tm_mon}_{tt.tm_mday}_{tt.tm_hour}_{tt.tm_min}_{tt.tm_sec}.txt'
    f = open(outputname, 'w+', encoding='UTF-8')
    for x in sorted(words):
        print(x, file=f)
    f.close()
    # t7_f = t.process_time_ns() #
    # print_intervalo(t7_i, t7_f) #

    print(f'Porcentaje usado: ', end='')
    print(f'{cant_presentes*100/total}%, ({cant_presentes}/{total}).')
    print(f'Si se agregan palabras faltantes al diccioanrio: ', end='')
    total = total + len(words)
    cant_presentes = cant_presentes + len(words)
    print(f'{cant_presentes*100/total}%, ({cant_presentes}/{total}).')