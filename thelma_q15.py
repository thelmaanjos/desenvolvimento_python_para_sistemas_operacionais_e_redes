import psutil, subprocess, time

def show_process_info():
    sp = subprocess.Popen("calc")
    p = psutil.Process(sp.pid)

    print(f"the process' PID is: {sp.pid}, its owner user name is {p.username()}, its creation date is {time.ctime(p.create_time())} and its memory usage is {round(p.memory_info()[0]/1024)} kb")

show_process_info()