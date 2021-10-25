import os

def print_absolute_path():
    path = 'thelma_q1.py'
    print('\n',os.path.abspath(path),'\n')

print_absolute_path()