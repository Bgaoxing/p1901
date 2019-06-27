import socket

# 因为主机是ipv4协议和tcp所以客户端一样使用ipv4和tcp

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41902)
# 客户端直接去链接地址，而不用去bind绑定地址并listen

client.connect(server_addr)

# 客户端不用写ip地址和端口号，socket帮助我们自动分配
client.send('我是客户端'.encode())
msg = client.recv(1460)
print('收到服务器发来的消息:', msg.decode())
client.close()
print('链接已经完成')