import psutil

def show_cpu_time_by_core(core_info):
    print(f'Number of cores: {psutil.cpu_count()}')
    for core in range(len(core_info)):
        print(f'Core {core+1} info: {core_info[core]}')

def main():
    core_info = psutil.cpu_times_percent(interval=0.1, percpu=True)
    show_cpu_time_by_core(core_info)

main()