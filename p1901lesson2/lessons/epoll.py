import socket, selectors
sel = selectors.DefaultSelector

def accept(sock, mask):
    """接受客户端"""
    conn, addr = sock.accept()
    print('新的链接', addr)
    conn.setblockink(False)
    sel.register(conn, selectors.EVENT_READ, read) # 新链接read回调函数

def read(conn, mask):
    """接受客户端数据"""
    date = conn.recv(65535)
    if date:
        print('新的消息', date)

