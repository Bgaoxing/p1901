import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket()
s.connect((HOST, PORT))

while True:
    msg = bytes(input('>>:'), encoding='utf8')
    s.sendall(msg)
    data = s.recv(1024)
    print('收到', data)
