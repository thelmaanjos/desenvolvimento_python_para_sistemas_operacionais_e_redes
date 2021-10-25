import os

def printAbsolutePath():
    path = 'thelma_q1.py'
    print('\n',os.path.abspath(path),'\n')

printAbsolutePath()