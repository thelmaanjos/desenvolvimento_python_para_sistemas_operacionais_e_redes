import psutil, os

def break_current_path_into_list(p, t, p0, p1, lista_dir):
    while p1: # fazer enquanto houver parte 1
        lista_dir.append(p1) # adiciona à lista a parte 1
        t = os.path.split(p0) # agora, separa p0
        p0 = t[0]
        p1 = t[1]
    lista_dir.append(p0) # Colocar último
    lista_dir.reverse() # Para reverter a lista, pois ela estava ao contrário
    return lista_dir

def get_current_dir_info(lista_dir):
    list_of_partitions = psutil.disk_partitions()
    print("//////////")
    for i in list_of_partitions:
        if i[0] == lista_dir[0]:
            disk_info = psutil.disk_usage(path=i[0])
            print(i)
            print(f'Device name: {i[0]}')
            print(f'File system type: {i[2]}')
            print(f'Total disk: {round(disk_info[0] / (1024 * 1024 * 1024), 2)} GB')
            print(f'Free disk: {round(disk_info[2] / (1024 * 1024 * 1024), 2)} GB')

def main():
    p = os.path.abspath('thelma_q20.py')
    t = os.path.split(p) # separa em duas partes
    p0 = t[0] # parte 0
    p1 = t[1] # parte 1
    lista_dir = []

    break_current_path_into_list(p, t, p0, p1, lista_dir)
    get_current_dir_info(lista_dir)

main()