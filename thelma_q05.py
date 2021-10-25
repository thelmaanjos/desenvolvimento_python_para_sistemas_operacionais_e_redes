import os

def doesFileExist(file_test):
  if os.path.exists(file_test):
    print(f'{file_test} exists!')
  else:
    print(f'{file_test} doesn\'t exist!')

def isFile(file_test):
  if os.path.isfile(file_test):
      print(f'{file_test} is a file!')
  else:
      print(f'{file_test} is not a file!')

def main():
  file_test = 'thelma_q1.py'
  doesFileExist(file_test)
  isFile(file_test)

main()