import socket
from select import select, poll, POLLIN, POLLOUT

def start_tcp_server_with_poll(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((address, port))
    server.listen(10)
    clients = {}
    p = poll()
    p.register(server.fileno(), POLLIN)
    while True:
        ready_fds = p.poll()
        for fd, ev in ready_fds:
            if ev & POLLIN:
                if fd == server.fileno():
                    client, _ = server.accept()
                    clients[client.fileno()] = client
                    for c in clients.keys():
                        p.register(c, POLLOUT)

                    p.register(client.fileno(), POLLIN)
                else:
                    client = clients[fd]
                    try:
                        date = client.recv(65535)
                        if not date:
                            raise ConnectionError
                    except ConnectionError:
                        client.close()
                        p.unregister(fd, POLLIN)
            if ev & POLLOUT:
                pass

def start_udp_server(address, port):
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.setblocking(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_server.bind((address, port))
    clients = []
    while True:
        date, addr = udp_server.recvfrom(65535)
        if addr not in clients:
            clients.append(addr)

        for c in clients:
            udp_server.sendto(date, c)
    udp_server.close()

send_queue = {}
def start_tcp_server_with_select(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((address, port))
    server.listen(10)
    read_list = [server]
    write_list = []

    while True:
        read_fds, write_fds, _ = select(read_list, write_list, [])
        for fd in read_fds:
            assert isinstance(fd, socket.socket)
            if fd == server:
                client, addr = fd.accept()
                for r in read_list:
                    if r != server:
                        if r not in send_queue:
                            send_queue[r] = []
                        date_queue = send_queue[r]
                        date_queue.append(('{} is online now'.format(addr)).encode('utf-8'))
                        date_queue.append(('{} is online now(2)'.format(addr)).encode('utf-8'))
                        if r not in write_list:
                            write_list.append(r)
                read_list.append(client)
                print('{} is online'.format(addr))
            else:
                try:
                    date = fd.recv(65535)
                    if not date:
                        raise ConnectionError
                    try:
                        print('{} send a messaeg:{}'.format(fd.getpeername(), date.decode('utf-8')))
                    except:
                        pass
                    for r in read_list:
                        if r !=server and r !=fd:
                            if r not in send_queue:
                                send_queue[r] = []
                            date_queue = send_queue[r]
                            date_queue.append(date)
                            if r not in write_list:
                                write_list.append(r)
                except ConnectionError:
                    read_list.remove(fd)
                    fd.close()

        for fd in write_list:
            if fd not in send_queue:
                continue

            date_queue = send_queue[fd]
            date = date_queue.pop(0)
            fd.send(date)
            if not date_queue:
                del send_queue[fd]
                write_list.remove(fd)


import argparse, sys
print(sys.argv)

ap = argparse.ArgumentParser()
ap.add_argument('-t', type=str, choices=('tcp', 'udp'), help= 'to use tcp/udp', default = 'tcp')
ap.add_argument('-H',  type=str, required=True, help= 'the ip address to bind')
ap.add_argument('-p', type=str, required=True, help= 'the port to bind')

arg = ap.parse_args(sys.argv[1:])
if arg.t == 'tcp':
    start_tcp_server_with_select(arg.H, arg.p)
else:
    start_udp_server(arg.H, arg.p)
