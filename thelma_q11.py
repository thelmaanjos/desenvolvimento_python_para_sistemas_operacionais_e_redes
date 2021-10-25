import os

def get_user_input():
    file_name = input("Enter the file name: ")
    return file_name

def doesFileExist(file_name):
  if os.path.exists(file_name):
    print(f'{file_name} exists!')
    print(os.path.abspath(file_name))  
    open_file = "notepad.exe " + file_name
    os.system(open_file)
  else:
    print(f'{file_name} doesn\'t exist!')

def main():
    file_name = get_user_input()
    doesFileExist(file_name)

main()