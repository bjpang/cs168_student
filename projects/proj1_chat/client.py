import sys
import socket

if __name__ == '__main__':
    client_socket = socket.socket()
    if len(sys.argv) == 3:
        client_socket.connect((sys.argv[1], int(sys.argv[2])))
        data = input('-->')
        client_socket.send(data.encode("utf-8"))
