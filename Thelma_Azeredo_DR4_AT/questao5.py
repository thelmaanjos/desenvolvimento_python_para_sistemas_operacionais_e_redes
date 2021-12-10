import os

def count_file_nums():
    splited_b_txt= list()
    splited_a_txt = list()
    splited_a_new_txt = []
    splited_b_new_txt = []
    sum_list = list()

    if os.path.exists("a.txt") and os.path.exists("b.txt"):
        a_txt = open("a.txt", "r")
        a_txt_readlines = a_txt.readlines()
        for i in a_txt_readlines:
            splited_a_txt = i.split(' ')
            #print(splited_a_txt)
        a_txt.close()
        for i in splited_a_txt:
            #print(i)
            splited_a_new_txt.append(int(i))

        b_txt = open("b.txt", "r")
        b_txt_readlines = b_txt.readlines()
        for i in b_txt_readlines:
            splited_b_txt = i.split(' ')
            #print(splited_b_txt)
        b_txt.close()
        for i in splited_b_txt:
            #print(i)
            splited_b_new_txt.append(int(i))

        count_difference = len(splited_a_new_txt) - len(splited_b_new_txt)

        if count_difference > 0:
            for i in range(0, count_difference):
                splited_b_new_txt.append(0)
        else:
            for i in range(0, count_difference):
                splited_a_new_txt.append(0)
        
        for a, b in zip(splited_a_new_txt, splited_b_new_txt):
            sum_list.append(sum([a, b]))
        
        for s in sum_list:
            print(s)
    else:
        print("No such files.")

count_file_nums()