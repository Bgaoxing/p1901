# import socket
#
# ss = socket.socket()
# #10.2.1.78
# addr = ('0.0.0.0',19523)
# ss.bind(addr)
#
# ss.listen()
# response_headers= """
# HTTP/1.1 200 OK
# Date: Wed, 03 Apr 2019 07:37:20 GMT
# Content-Type: text/html;charset=UTF-8
# Transfer-Encoding: chunked
# Vary: Accept-Encoding
# Cache-Control: max-age=86400
# X-Via-JSL: 2239390,mem(2.4.2)
# Expires: Thu, 04 Apr 2019 07:37:20 GMT
# X-Cache: hit
# Content-Encoding: gzip
# """
# response_tab = "\r\n"
#
# response_body = "hhhhhhhhhhh"
#
# response = response_headers + response_tab + response_body
# while 1:
#     conn,addr = ss.accept()
#     print('你有新的连接{}'.format(addr))
#
#     msg = conn.recv(65535)
#     print(msg.decode())
#     conn.send(response.encode())

import socket
ss = socket.socket()
addr = ('localhost', 19234)
ss.bind(addr)
ss.listen()
print('服务器开启')
response_header = """
http/1.1 20 ok\r\n\r\n
hello word
"""
while 1:
    conn, addr = ss.accept()
    print('你有新的链接{}'.format(addr))
    msg = conn.recv(65535)
    print(msg.decode())
    conn.send(response_header.encode())



