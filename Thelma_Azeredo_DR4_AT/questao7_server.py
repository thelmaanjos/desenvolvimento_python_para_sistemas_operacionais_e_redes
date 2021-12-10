import socket, psutil

def memory_usage():
    mem = psutil.virtual_memory()
    
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    available = round(mem.available / (1024 * 1024 * 1024), 2)
    used = round(mem.used / (1024 * 1024 * 1024), 2)
    free = round(mem.free / (1024 * 1024 * 1024), 2)
    
    return "\n" + "Total memory: " + str(total) + "GB" + " " + "Memory available: " + str(available) + "GB" + " " +  "Memory used: " + str(used) + "GB" + " " +  "Free memory: " + str(free) + "GB" + " " +  "Memory percent: " + str(mem.percent) + "%" + "\n"

def client_conn(orig):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(orig)
    flag = True

    while flag:
        (msg, client) = udp.recvfrom(1024)

        if 'Memory info' == msg.decode('utf-8'):
           msg = memory_usage()
        else:
            print("Closing connection with", str(client), "...")
            input("Press any key to close the connection")
            udp.close()
            flag = False
        udp.sendto (msg.encode('utf-8'), client)
    
def main():
    HOST = ''
    PORT = 9991
    orig = (HOST, PORT)
    print(f'Waiting for client on port {PORT}')
    client_conn(orig)

main()