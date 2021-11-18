import socket, sys, os

def server_conn(client_socket, file_name):
    try:
        client_socket.connect((socket.gethostname(), 8881))
        client_socket.send(file_name.encode('ascii'))
        msg = client_socket.recv(1024)
        file_size = int(msg.decode('ascii'))
        if file_size >= 0:
            print('File size: ', file_size)
            file_name = os.path.basename(file_name)
            
            with open(file_name, 'wb+') as file:
                sum = 0
                txt_bytes = client_socket.recv(4096)
                
                while txt_bytes:
                    file.write(txt_bytes)
                    sum = sum + len(txt_bytes)
                    print('Downloading...', sum, 'kb', file_size, 'bytes')
                    txt_bytes = client_socket.recv(4096)
        else:
            print('The server could not find the file.')
    except Exception as error:
        raise
    client_socket.close()
    print('Press any key to close the connection')

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_name = input('Enter the file name: ')

    server_conn(client_socket, file_name)

main()