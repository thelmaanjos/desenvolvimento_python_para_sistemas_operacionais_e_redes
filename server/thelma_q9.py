import socket, psutil

def disk_usage():
    disk = psutil.disk_usage('.')  
    total = round(disk.total/(1024*1024*1024), 2)
    using = round(disk.used/(1024*1024*1024), 2)
    free = round(disk.free/(1024*1024*1024), 2)

    return "\n" + "Total disk: " + str(total) + "GB" + " " + "Disk in use: " + str(using) + "GB" + " " +  "Disk available: " + str(free) + "GB" + " " +  "Disk percent: " + str(disk.percent) + "%" + "\n"

def client_conn(orig):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(orig)
    flag = True

    while flag:
        (msg, client) = udp.recvfrom(1024)

        if '2' == msg.decode('utf-8'):
            print("Closing connection with", str(client), "...")
            input("Press any key to close the connection")
            udp.close()
            flag = False
        else:
            msg = disk_usage()
        udp.sendto (msg.encode('utf-8'), client)
    
def main():
    HOST = ''
    PORT = 9991
    orig = (HOST, PORT)
    print(f'Waiting for client on port {PORT}')
    client_conn(orig)

main()