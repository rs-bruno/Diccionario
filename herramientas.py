#   Herramientas de manipulación del diccionario.
#   Éstas funciones asumen la existencia de los siguientes archivos:
#       Textos\palabras.txt
#       Textos\verbos_irregulares_infinitivos.txt
#       Textos\verbos_irregulares_conugados.txt
#       Textos\verbos_regulares_infinitivos.txt
#       Textos\verbos_regulares_conjugados.txt
#       Textos\sus_adj.txt
#   La funcionalidad del módulo depende de dichos archivos.
import time

n_int = [0]
def print_intervalo(a,b,c):
    print(f'Intervalo {c[0]} = {(b-a)/1000**2}ms')
    c[0] = c[0] + 1

t_a = time.process_time_ns()

palabras_f = open(r'Textos\palabras.txt', 'r', encoding='UTF-8')
palabras_set = {w[:len(w)-1] for w in palabras_f} #Se quitan los sufijos '\n'
palabras_f.close()

t_b = time.process_time_ns()
print_intervalo(t_a, t_b, n_int)

irregulares_f = open(r'Textos\verbos_irregulares_conjugados.txt', 'r', encoding='UTF-8')
irregulares_set = {w[:len(w)-1] for w in irregulares_f}
irregulares_f.close()

t_c = time.process_time_ns()
print_intervalo(t_b, t_c, n_int)

palabras_set = palabras_set | irregulares_set

t_d = time.process_time_ns()
print_intervalo(t_c, t_d, n_int)


regulares_f = open(r'Textos\verbos_regulares_conjugados.txt', 'r', encoding='UTF-8')
regulares_set = {w[:len(w)-1] for w in regulares_f}
regulares_f.seek(0)
regulares_list = [w[:len(w)-1] for w in regulares_f]
regulares_f.close()

t_e = time.process_time_ns()
print_intervalo(t_d, t_e, n_int)

sus_adj_f = open(r'Textos\sus_adj.txt', 'r', encoding='UTF-8')
sus_adj_set = {w[:len(w)-1] for w in sus_adj_f}
sus_adj_f.seek(0)
sus_adj_list = [w[:len(w)-1] for w in sus_adj_f]
sus_adj_f.close()

t_f = time.process_time_ns()
print_intervalo(t_e, t_f, n_int)

def noalpha_to_space(linea):
    buff = ''
    for caracter in linea:
        if not caracter.isalpha():
            buff = buff + ' '
        else:
            buff = buff + caracter
    return buff

def porcentuar(path):
    '''Calcula una estimación del porcentaje del lenguaje utilizado.'''
    f = open(path, 'r', encoding='UTF-8')
    lines_raw = f.readlines()
    f.close()
    lines_clean = []
    for l_r in lines_raw:
        lines_clean.append(noalpha_to_space(l_r))
    words = {'0'}
    words.remove('0')
    for l_c in lines_clean:
        aux = [w.lower() for w in l_c.split()]
        words.update(aux)
    total = len(palabras_set)
    cant_presentes = 0
    for p in palabras_set:
        if p in words:
            cant_presentes = cant_presentes + 1
            words.remove(p)
    bools_verbos_regulares = [False for x in range(len(regulares_list) // 53)]
    bools_sus_adj = [False for x in range(len(sus_adj_list) // 4)]
    a_quitar = {'0'}
    a_quitar.remove('0')
    for w in words:
        if w in regulares_set:
            a_quitar.add(w)
            indice = regulares_list.index(w) // 53
            if not bools_verbos_regulares[indice]:
                cant_presentes = cant_presentes + 1
                bools_verbos_regulares[indice] = True
        elif w in sus_adj_set:
            a_quitar.add(w)
            indice = sus_adj_list.index(w) // 4
            if not bools_sus_adj[indice]:
                cant_presentes = cant_presentes + 1
                bools_sus_adj[indice] = True
    words = words - a_quitar
    t = time.localtime()
    outputname = f'ausentes_{t.tm_year}_{t.tm_mon}_{t.tm_mday}_{t.tm_hour}_{t.tm_min}_{t.tm_sec}.txt'
    f = open(outputname, 'w+', encoding='UTF-8')
    for x in sorted(words):
        print(x, file=f)
    f.close()
    print(f'Porcentaje usado: ', end='')
    print(f'{cant_presentes*100/total}%, ({cant_presentes}/{total}).')
    print(f'Si se agregan palabras faltantes al diccioanrio: ', end='')
    total = total + len(words)
    cant_presentes = cant_presentes + len(words)
    print(f'{cant_presentes*100/total}%, ({cant_presentes}/{total}).')