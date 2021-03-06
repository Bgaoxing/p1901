# import socket
# from threading import Thread
#
# conn_lists = list()
#
#
# def handle_conn(conn, addr):
#     while 1:
#         msg = conn.recv(65535)
#         return_msg = '地址在{}的用户说:{}'.format(addr, msg.decode())
#         for conn in conn_lists:
#             conn.send(return_msg.encode())
#
#
# def conn_server(addr):
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind(addr)
#     ss.listen()
#     print('服务器已经启动')
#     # 会阻塞 等待链接进来
#
#     while 1:
#         conn, addr = ss.accept()
#         conn_lists.append(conn)
#         print('新来链接,地址{}'.format(addr))
#         handle = Thread(target=handle_conn, args=(conn, addr))
#         handle.start()
#
#
# if __name__ == "__main__":
#     addr = ("127.0.0.1", 9520)
#     conn_server(addr)


import socket
from threading import Thread
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 23433)
conn_list = list()
def conn_ser(addr):
    ss.bind(addr)
    ss.listen()
    print('开启')
    while 1:
        conn, addr = ss.accept()
        conn_list.append(conn)
        print('新用户链接,地址为{}'.format(addr))
        hander = Thread(target=hander_conn, args=(conn, addr))
        hander.start()
def hander_conn(conn, addr):
    while 1:
        msg = conn.recv(65535)
        return_msg = '地址为{}的用户说{}'.format(addr, msg.decode())
        print(return_msg)
        for conn in conn_list:
            conn.send(return_msg.encode())
if __name__ == '__main__':
    conn_ser(addr)
