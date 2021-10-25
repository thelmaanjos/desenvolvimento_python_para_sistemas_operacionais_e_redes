import subprocess

def create_process():
    sp = subprocess.Popen("notepad")
    print(f"the process' PID is: {sp.pid}")

create_process()