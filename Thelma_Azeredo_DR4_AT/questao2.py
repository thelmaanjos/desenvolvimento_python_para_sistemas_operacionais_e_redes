
import subprocess, os

def create_notepad_subprocess():
    file_name = input("Enter the notepad file name: ") 
    p = subprocess.Popen(["notepad", file_name])

    if os.path.exists(file_name):
        print(file_name, 'exists!')
        print(file_name,"'s created process PID:", p.pid)
    else:
        print(p, 'does not exist.')

create_notepad_subprocess()