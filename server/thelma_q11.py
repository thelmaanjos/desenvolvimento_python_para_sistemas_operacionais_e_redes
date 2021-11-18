import socket, os

def client_conn(server_socket):
    while True:
        (client_socket, addr) = server_socket.accept()
        print('Connected to: ', str(addr))
        msg = client_socket.recv(2048) 
        file_name = msg.decode('ascii')
        print(file_name)

        if os.path.isfile(file_name):
            size = os.stat(file_name).st_size
            print(size)
            client_socket.send(str(size).encode('ascii'))
            file = open(file_name, 'rb')
            info_bytes = file.read(4096)
            while info_bytes:
                client_socket.send(info_bytes)
                info_bytes = file.read(4096)
            file.close()
        else:
            print('File not found.')
            client_socket.send(b'-1')
        client_socket.close()
    server_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                        
    PORT = 8881
    HOST = socket.gethostname()
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server", HOST, "waiting on port", PORT)

    client_conn(server_socket)

main()
