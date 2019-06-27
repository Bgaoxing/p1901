from gglib.link import list
from threading import Condition
from threading import Lock
from threading import Thread

lock = Lock()
cond = Condition(lock)
l = list()


def consumer(*args, **kwargs):
    print("The consumer is ready to read.")
    while True:
        cond.acquire()
        if l:
            data = l.pop()
            print("\n" + data)
        else:
            cond.wait()
        cond.release()


consume_thread = Thread(target=consumer)
consume_thread.start()

while True:
    data = input("Please enter: ")
    cond.acquire()
    l.append(data)
    cond.notify()
    cond.release()
