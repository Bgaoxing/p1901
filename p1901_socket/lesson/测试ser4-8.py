"""
P1901socket编程试题(考试时间 2小时):

题目: 实现一个多人聊天室

	要求:  1. 至少实现一个服务端客户端(C/S模式) 的聊天室 服务端和客户端代码 (0-40分)
			2. 能够进行多人同时和服务器收发消息的 服务端和客户端代码 (40-60分)
			3. 能够实现多人同时和服务器收发消息,并且服务器会广播消息的 服务端和客户端代码 (60-70分)
			4. 能够使用线程池来实现上面功能(70-80分)
			5. 能够在完成4要求的情况下考虑到多线程切换的问题,并且对合适的地方上锁,并说明为什么要上锁 (80-90分)
			6. 能够在完成5的要求下实现客户端能顺利关闭退出,并且其他客户端能收到有客户端退出的消息,并且整体代码无bug (90-100分)

	提交方式:将代码发至我微信
	作弊判断规则: 若出现多人代码样视为作弊,多人全部0分
"""

import socket
from threading import RLock
from concurrent.futures import ThreadPoolExecutor
from functools import partial
conn_lists = list()
lock = RLock()
pools = ThreadPoolExecutor(max_workers=20)

def handle_conn(conn, addr):
    while 1:
        msg = conn.recv(65535)
        return_msg = '地址在{}的用户说:{}'.format(addr, msg.decode())
        lock.acquire()
        for conn in conn_lists:
            conn.send(return_msg.encode())
        lock.release()

def conn_server(addr):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(addr)
    ss.listen()
    print('服务器已经启动')
    # 会阻塞 等待链接进来

    while 1:
        conn, addr = ss.accept()
        conn_lists.append(conn)
        print('新来链接,地址{}'.format(addr))
        pools.submit(partial(handle_conn, conn, addr))


if __name__ == "__main__":
    addr = ("127.0.0.1", 9520)
    conn_server(addr)
