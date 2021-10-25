import psutil

def get_free_size_of_disk():
    list_of_partitions = psutil.disk_partitions()
    installed_system_path = list_of_partitions[0][0] # programs are usually installed in C:
    disk_info = psutil.disk_usage(path=installed_system_path)
    
    print(f'Free disk size is: {round(disk_info[2] / (1024 * 1024 * 1024), 2)} GB')

get_free_size_of_disk()