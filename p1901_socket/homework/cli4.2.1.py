# import socket
# from threading import Thread
# ss = socket.socket()
# ss.connect(('127.0.0.1', 9520))
#
# def conn_send(ss):
#     while 1:
#         msg = input('请输入消息:')
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
#     print('接收程序已经结束')
#
# t1 = Thread(target=conn_send,args=(ss,))
# t2 = Thread(target=conn_recv,args=(ss,))
#
# t1.start()
# t2.start()
# print('聊天客户端已经启动')
# t1.join()
# t2.join()
# print('聊天客户端已经结束')


import socket
from threading import Thread
ss = socket.socket()
ss.connect(('localhost', 23433))
def send():
    while 1:

        msg = input('输入消息:')
        try:
            ss.send(msg.encode())
        except Exception:
            break
    print('发送完成')
def recv():
    while 1:
        return_msg = ss.recv(65535)
        if not return_msg:
            break
        print(return_msg.decode())
    print('接受完成')
t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()
t1.join()
t2.join()
print('结束')