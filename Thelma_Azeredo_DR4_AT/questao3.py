import os

def search_specific_dir():
    lista_dir = []
    lista_arq = []
    size_list = []
    p_dir = ""
    dir_path = input("\nEnter the full dir path: ")
    
    if os.path.isdir(dir_path):
        lista_dir.append(dir_path)
        sum = 0

        while lista_dir:
            dir = lista_dir[0]
            p_dir = os.path.join(p_dir, dir)
            lista = os.listdir(p_dir)
            for i in lista:
                p = os.path.join(p_dir, i)
                size = os.stat(p).st_size
                
                if os.path.isfile(p):
                    lista_arq.append([i, size])
                    size_list.append(size)
                    sum = sum + size
            lista_dir.remove(dir)
        if len(lista_arq) > 0:
            print("\nFiles:")
            size_list.sort(reverse=True)
            for i in size_list:
                for j in lista_arq:
                    if j[1] == i:
                        print(j)
        print(" ")
        print("Those files are a total of "+ str(sum/1024) + " KB")
        
        arq = open("kbs.txt", "w")
        arq.write(str(size_list))
        arq.close()

    else:
        print("Dir", '\''+ dir_path +'\'', "does not exist.")

search_specific_dir()