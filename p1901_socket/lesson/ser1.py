#引用socket 库，python装了就有
import socket
#使用方法

# 1 初始化socket对象
# socket里面，第一个写使用哪个网络层协议，第二个写哪个运输层协议
# 网络层 ocket.AF_INET表示使用ipv4协议，socket.AF_INET6表示ipv6
# 运输层 socket.SOCK_STREAM表示的tcp协议，SOCK_STREAM 表示udp协议

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 绑定ip和端口

# 127.0.0.1 -->本地回环网 loop 如果绑定该地址，其他人不能访问
# 0.0.0.0 -->会自动换算路由器分配的局域网地址 相当于10.2.1.78
# 255.255.255.255 -->广播地址
# 10.2.1.78 -->局域网地址
server_addr = ('0.0.0.0', 41902)
server.bind(server_addr)
print('服务器已经开启')

# 3 监听这个地址socket.AF_INET
server.listen()

# 4 监听这个地址后需要接受服务
# conn表示链接对象，addr表示链接地址
# 有链接进来才会执行，无链接进来就会阻塞
conn, conn_addr = server.accept()
# conn是一个对象
# 1460 一次性收1460byte的消息
# mss 报文最大量，tcp默认1460 因为链路层一般最大能接受1500b数据
# tcp 20b ip 20b 1500-40 = 1460b
# 理论最大值 65535- 40 = 65495b

msg = conn.recv(1460)
# 收到的消息是二进制
# 把二进制数据转换成字符串
print('收到客户端发来的消息:', msg.decode())
# conn_addr是一个tuple
return_msg = "消息已经收到"
# 加上encode 把普通字符变成二进制
conn.send(return_msg. encode())


conn.close()
server.close()
print(conn_addr)

print('服务器已经结束')
