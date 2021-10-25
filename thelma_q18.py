import psutil

def print_total_memory(main_mem, swap_mem):
    print(f'Main memory: {round(main_mem / (1024 * 1024 * 1024), 2)} GB')
    print(f'Swap memory: {round(swap_mem / (1024 * 1024 * 1024), 2)} GB')

def main():
    swap_mem = psutil.swap_memory().total
    main_mem = psutil.virtual_memory().total
    print_total_memory(main_mem, swap_mem)

main()