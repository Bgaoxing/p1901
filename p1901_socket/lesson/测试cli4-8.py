# import socket
# import sys
# from threading import Thread
# ss = socket.socket()
# ss.connect(('127.0.0.1', 19521))
#
# def conn_send(ss, addr):
#     while 1:
#         msg = input('请输入消息(quite退出):')
#         # if msg == 'quite':
#         #     ss.sendto(msg.encode(), addr)
#         #     sys.exit('退出聊天室')
#
#         try:
#             ss.send(msg.encode())
#         except Exception:
#             break
#     print('发送程序已经结束')
#
# def conn_recv(ss):
#     while 1:
#         return_msg = ss.recv(65535)
#         if not return_msg:
#             break
#         print(return_msg.decode())
#     print('     ')
#     print('接收程序已经结束')
#
# t1 = Thread(target=conn_send, args=(ss,))
# t2 = Thread(target=conn_recv, args=(ss,))
#
# t1.start()
# t2.start()
# print('进入聊天室')
# t1.join()
# t2.join()
# print('离开聊天室')

import socket
from threading import Thread
ss = socket.socket()
ss.connect(('127.0.0.1', 12345))
def send(ss):
    while 1:
        msg = input('输入消息:')
        try:
            ss.send(msg.encode())
        except Exception:
            break
        print('发送结束')

def recv(ss):
    while 1:
        return_msg = ss.recv(65535)
        if not return_msg:
            break
        print(return_msg.decode())
    print('  ')
    print('接收完成')
t1 = Thread(target=send, args=(ss,))
t2 = Thread(target=recv, args=(ss,))
t1.start()
t2.start()
print('进入聊天')
t1.join()
t2.join()
print('离开')