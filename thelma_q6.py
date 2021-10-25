import os

def get_file_extension(filename):
   ext = os.path.splitext(filename)[1]
   print(f'This file extension is {ext}')

def main():
    filename = 'thelma_q1.py'
    get_file_extension(filename)

main()