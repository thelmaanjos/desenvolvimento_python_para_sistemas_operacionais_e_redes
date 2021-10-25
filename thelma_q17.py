import psutil, time
psutil.cpu_percent(percpu=True)

def show_cpu_info_by_second(core_info):
    print(f'Number of cores: {psutil.cpu_count()}')
    for i in range(20):
        print(f'Loop block {i + 1}')
        for core in range(len(core_info)):
            print(f'Core {core+1} info: {core_info[core]}')
            time.sleep(1)

def main():
    core_info = psutil.cpu_times_percent(interval=1, percpu=True)
    show_cpu_info_by_second(core_info)

main()

