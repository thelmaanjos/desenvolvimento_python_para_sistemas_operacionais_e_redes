import os

def get_user_input():
    file_name = input("Enter the file name:")
    return file_name

def doesFileExist(file_name):
  if os.path.exists(file_name):
    print(f'{file_name} exists!')
    print(os.path.abspath(file_name))
  else:
    print(f'{file_name} doesn\'t exist!')

def isFile(file_name):
  if os.path.isfile(file_name):
      print(f'{file_name} is a file!')
  else:
      print(f'{file_name} is not a file!')

def main():
    file_name = get_user_input()
    doesFileExist(file_name)
    isFile(file_name)
    
  

main()