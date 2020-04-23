import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    msg = clientsocket.recv(1024)
    cmd = msg.decode("utf-8")

    if cmd:
        t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t.connect(("execute-node", 1235))
        t.send(bytes(cmd, "utf-8"))
