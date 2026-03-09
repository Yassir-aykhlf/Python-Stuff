import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg = sys.argv[1] if len(sys.argv) > 1 else 'Hello, server!'

with client:
    client.connect(('127.0.0.1', 25565))
    client.sendall(msg.encode())
    data = client.recv(1024)
    print('Received from server:', data.decode())
