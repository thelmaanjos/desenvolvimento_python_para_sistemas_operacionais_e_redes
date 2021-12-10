import os 

def reverse_text():
    file_name = "arquivo.txt"
    arch = open(file_name, "r")

    if os.path.exists(file_name):
        reversed_txt = arch.readlines()
        for line in reversed(reversed_txt):
            print(line[::-1], end="")
        arch.close()
    else:
        print("No such a file exists.")

reverse_text()