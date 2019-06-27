from gglib.link import list
from threading import Condition # 条件
from threading import Lock
from threading import Thread

lock = Lock()
cond = Condition(lock)
l = list()


def consumer(*args, **kwargs):
    print("The consumer is ready to read.")

    while True:
        cond.acquire()
        while 1:
            if len(l) >= 1:
                data = l.pop()
                print("\n" + data)
            else:
                cond.wait()
                cond.notify()
                break
        cond.release()


consume_thread = Thread(target=consumer)
consume_thread.start()


while True:
    cond.acquire()
    while 1:
        if len(l) < 5:
            data = input("Please enter: ")
            l.append(data)
        else:
            cond.notify()  # 通知
            cond.wait()
            break
    cond.release()