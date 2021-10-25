import os

def get_files(files, list_of_files):
    for file in files:
        list_of_files.append(file)
    return list_of_files

def get_files_and_kbs(list_of_files, files_and_sizes):
    for file in list_of_files:
        files_and_sizes.append([file, str(os.stat(file).st_size / 1024) + ' kb'])
    return files_and_sizes

def main():
    list_of_files = []
    files_and_sizes = list()
    files = os.listdir('.')

    get_files(files, list_of_files)
    print(get_files_and_kbs(list_of_files, files_and_sizes))

main()