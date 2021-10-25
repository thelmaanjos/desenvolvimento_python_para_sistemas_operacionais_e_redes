import os, platform

def print_PID(pid, os_name):
    try:
        if os_name == 'Linux':
            gid = os.getgid()
            print(f'This process\' gid is {gid} ')
        else:
            print(f'This process\' pid is {pid} ')
    except AttributeError:
        print('module \'os\' has no attribute \'getgid\'')

def main():
    pid = os.getpid()
    os_name = platform.system()
    print_PID(pid, os_name)

main()