import socket
import pickle

def server_conn(client_socket, client_host, port, dir_name):
    try:
        client_socket.connect((client_host, port))
        client_socket.send(dir_name.encode('ascii'))
        msg = client_socket.recv(4096)
        l_msg = pickle.loads(msg)
        print("The following files were found:")
        for file in l_msg:
            print(file)
    except Exception as err:
        raise
        client_socket.close()
    input("Press any key to end connection...")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_host = socket.gethostname()
    port = 8881
    dir_name = input('Enter the directory name: ')
    server_conn(client_socket, client_host, port, dir_name)

main()