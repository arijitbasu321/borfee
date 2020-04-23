import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("master-node", 1234))
s.send(bytes("date", "utf-8"))
