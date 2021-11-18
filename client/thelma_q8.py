import socket

def server_conn(dest):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    flag = True
    while flag:
        menu = input('Welcome. \n1 - ask for disk info \n2 - exit \nChoose one option:\n')
        udp.sendto (menu.encode('utf-8'), dest)

        if menu == '1': 
            (menu, servidor) = udp.recvfrom(1024)
            print(servidor, menu.decode('utf-8'))
        elif menu == '2':
            print("Goodbye.")
            udp.close()
            flag = False
        else:
            print("\n Not a valid choice, try again")

def main():
    HOST = socket.gethostname() 
    PORT = 9991 

    dest = (HOST, PORT)
    server_conn(dest)

main()