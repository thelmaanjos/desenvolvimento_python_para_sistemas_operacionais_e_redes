import socket
import os
import pickle

def client_conn(server_socket):
    while True:
        (socket_client, addr) = server_socket.accept()
        print("Connected to...:", str(addr))
        msg = socket_client.recv(2048)
        dir_name = msg.decode('ascii')
        client_list = get_client_info(dir_name)
        msg = pickle.dumps(client_list)
        socket_client.send(msg)
        socket_client.close()

def get_client_info(dir):
    file_list = []

    if os.path.exists(dir):
       list_dir = os.listdir(dir)
    else:
        print("This dir does not exist.")
    
    for li in list_dir:
        if os.path.isfile(li):
            file_list.append(li)
        elif os.path.isdir(li):
            pass
        else:
            print("Error, try connecting again.")
    return file_list

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = socket.gethostname()
    port = 8881
    server_socket.bind((server_host, port))
    server_socket.listen()
    print(f"Server {server_host} waiting for connection at port {port}.")
    client_conn(server_socket)

main()