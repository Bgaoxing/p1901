from gglib.request import Request


class SessionClosedError(BaseException):
    pass


class Session:
    _sessions = dict()

    def __init__(self, sock):
        self.sock = sock
        Session._sessions[sock] = self

    def close(self):
        if self.sock in Session._sessions:
            del Session._sessions[self.sock]
        self.sock.close()

    def recv_request(self):
        try:
            session = Session.get_session_by_sock(self.sock)
            data = self.sock.recv(65535)
            # 如果客户端关闭连接
            if not data:
                raise ConnectionError
            request = Request(session, data)
            return request
        except ConnectionError:
            # 清理客户端套接字对象
            self.close()
            raise SessionClosedError


    @classmethod
    def get_session_by_sock(cls, sock):
        return Session._sessions[sock]