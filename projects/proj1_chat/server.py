import socket

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 80))
    server_socket.listen(3)
    (new_sock, address) = server_socket.accept()
    print(new_sock.recv(4096))
