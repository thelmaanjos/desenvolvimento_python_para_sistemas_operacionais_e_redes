import psutil, time

# https://lms.infnet.edu.br/moodle/mod/page/view.php?id=253509&forceview=1

def show_subprocess_info(pid):
    try:
        p = psutil.Process(pid)
        texto = '{:6}'.format(pid)
        texto = texto + '{:11}'.format(p.num_threads())
        texto = texto + " " + time.ctime(p.create_time()) + " "
        texto = texto + '{:8.2f}'.format(p.cpu_times().user)
        texto = texto + '{:8.2f}'.format(p.cpu_times().system)
        texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
        rss = p.memory_info().rss/1024/1024
        texto = texto + '{:10.2f}'.format(rss) + " MB"
        vms = p.memory_info().vms/1024/1024
        texto = texto + '{:10.2f}'.format(vms) + " MB"
        texto = texto + " " + p.exe()
        print(texto)
    except:
        pass

def list_all_running_processes():
    li= psutil.pids()
    print("List of all running processes: ")
    for i in li:
        show_subprocess_info(i)
    print("Finished listing all the running processes.")

def search_for_specific_process(pids_name):
    lp = psutil.pids()
    pid_list = []
    
    for i in lp:
        p = psutil.Process(i)
        if p.name() == pids_name:
            pid_list.append(str(i))

            print(p)
            print("'%' of CPU use:", p.cpu_percent(interval=1.0), "%")
            perc_mem = '{:.2f}'.format(p.memory_percent())
            print("'%' of memory use:", perc_mem, "%")
            mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
            print("Memory use:", mem, "MB")
            print(" ")
    
    if len(pid_list) > 0:
        print(pids_name,"'s PID(s) is/are: ")
        print(', '.join(pid_list))

    else:
        print(pids_name, "is currently not being executed.")
    

def main():
    list_all_running_processes()
    pids_name = input("\nEnter the PID's name to be searched: ")
    search_for_specific_process(pids_name)

main()
    