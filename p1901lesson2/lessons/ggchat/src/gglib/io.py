
# 设置套接字(socket)大小
# 发送访问大小
# 接收访问大小
# 绑定地址
# 监听
# 等待连接
# 关闭
# daemon 创建子线程, daemon=True 守护主线程， 主线程退出后子线程直接销毁不再执行子线程的代码
# IO多路复用中包括 select、pool、epoll，这些都属于同步

import socket
import select

from gglib.handlers import handle
from gglib.queue_ex import Queue
from gglib.session import Session, SessionClosedError
from gglib.settings import IO, NUM_WORKERS
import threadpool


# 创建工作者线程池，与请求队列
thread_pool = threadpool.ThreadPool(NUM_WORKERS)
request_queue = Queue(10000)

def wait_request_to_process():
    while True:
        request = request_queue.get(block=True)
        handle(request)

# 启动工作者线程并等待请求去处理
for t in range(NUM_WORKERS):
    request = threadpool.WorkRequest(callable_=wait_request_to_process)
    thread_pool.putRequest(request)

# 创建服务器套接口
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字选项
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, IO['SZ_SEND_BUFFER'])
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, IO['SZ_RECV_BUFFER'])
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #
_socket.setblocking(False)

_socket.bind(IO['BIND_ADDRESS'])
_socket.listen(10)

_read_list = [_socket]
_write_list = []
_except_list = [] # 异常

while True:
    # 使用IO复用技术
    _ready_rlist, _ready_wlist, _ready_xlist = select.select(_read_list,
                                                             _write_list,
                                                             _except_list)
    for fd in _ready_rlist:
        if fd == _socket:
            # 接受远程连接，并为该客户端创建会话
            client, addr = _socket.accept()
            session = Session(client)
            _read_list.append(client)
            continue
        else:
            assert isinstance(fd, socket.socket)
            try:
                # 处理会话，并队列化请求
                session = Session.get_session_by_sock(fd)
                request = session.recv_request()
                request_queue.put(request)
            except SessionClosedError:
                # 清理客户端套接字对象
                _read_list.remove(fd)