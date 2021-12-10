import time
import threading
from random import randint

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calculate_fatorial(vet1, vet2, start, end):
    for v in vet1[start:end]:
        fact = fatorial(v)
        vet2.append(fact)

def factorial_threading(vet1, vet2, list_of_threads, num_of_threads, list_size, vect_size):
    start = float(time.time())

    for v in range(vect_size):
        vet1.append(randint(0, vect_size))
        list_size = len(vet1)

    for t in range(num_of_threads):
        start = t * int(list_size/num_of_threads)
        end = (t + 1) * int(list_size/num_of_threads)
        th = threading.Thread(target=calculate_fatorial, args=(vet1, vet2, start, end))
        th.start()
        list_of_threads.append(th)

    for lt in list_of_threads:
        lt.join()
        
    finish = float(time.time())
    
    print(vet2)
    print(f"Execution time: {finish - start}")

def main():
    vet1 = [10, 15, 20, 17]
    vet2 = []
    vect_size = 1000
    list_size = len(vet1)
    list_of_threads = []
    num_of_threads = 4
    factorial_threading(vet1, vet2, list_of_threads, num_of_threads, list_size, vect_size)

main()