import multiprocessing
import time
import random

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calculate_factorial(q_input, q_output):
    fact_list = q_input.get()
    vet = []
    
    for f in fact_list:
        fact = fatorial(f)
        vet.append(fact)
    q_output.put(vet)

if __name__ == "__main__":
    vet1 = []
    vet2 = []
    vet_size = 100
    process_num = 4
    process_list = []
    q_input = multiprocessing.Queue()
    q_output = multiprocessing.Queue()

    start = float(time.time()) 

    for i in range(vet_size):
        vet1.append(random.randint(0, 20))

    for i in range(process_num):
        start = i * int(vet_size/process_num)
        end = (i + 1) * int(vet_size/process_num)
        q_input.put(vet1[start:end])
        m = multiprocessing.Process(target=calculate_factorial, args=(q_input, q_output))
        m.start()
        process_list.append(m)

    for m in process_list:
        m.join()

    for i in range(0, process_num):
        for q in q_output.get():
            vet2.append(q)
    
    finish= float(time.time())

    print(vet2)
    print(f"Execution time: {finish - start}")
