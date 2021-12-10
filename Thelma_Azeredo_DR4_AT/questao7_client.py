import socket

def server_conn(dest):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.settimeout(5)
    flag = True
    while flag:
        try:
            msg = "Memory info"
            udp.sendto (msg.encode('utf-8'), dest)
            (msg, servidor) = udp.recvfrom(1024)
            print(servidor, msg.decode('utf-8'))
        except socket.timeout:
            udp.close()
            print("Goodbye.")
            udp.close()
            flag = False

def main():
    HOST = socket.gethostname() 
    PORT = 9991 
    dest = (HOST, PORT)
    server_conn(dest)

main()