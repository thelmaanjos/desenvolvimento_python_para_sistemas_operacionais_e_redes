import time
from random import randint

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def append_factorial(vet1, vet2):
    for v in vet1:
        fact = fatorial(v)
        vet2.append(fact)
    print(vet2)

def calculate_factorial(vet_size, vet1, vet2):
    start = float(time.time())
    
    for i in range(vet_size):
        vet1.append(randint(0, vet_size))
    for v in vet1:
        fact = fatorial(v)
        vet2.append(fact)
        
    finish = float(time.time())
    print(f"Execution time: {finish - start}")

def main():
    vet1 = [5, 10, 15, 20, 25]
    vet2 = []
    vet_size = 100
    append_factorial(vet1,vet2)
    calculate_factorial(vet_size, vet1, vet2)

main()