import os

def does_file_exist(file_test):
  if os.path.exists(file_test):
    print(f'{file_test} exists!')
  else:
    print(f'{file_test} doesn\'t exist!')

def is_file(file_test):
  if os.path.isfile(file_test):
      print(f'{file_test} is a file!')
  else:
      print(f'{file_test} is not a file!')

def main():
  file_test = 'thelma_q1.py'
  does_file_exist(file_test)
  is_file(file_test)

main()