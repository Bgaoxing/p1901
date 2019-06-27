from gglib.link import list
from threading import Lock
from threading import Condition


class QueueEmpty(BaseException):
    pass


class QueueFull(BaseException):
    pass


class Queue:
    def __init__(self, maxsize):
        self.max_size = maxsize
        self._queue = list()
        self._rlock = Lock()
        self._wlock = Lock()
        self._read_cond = Condition(self._rlock)
        self._write_cond = Condition(self._wlock)

    def is_full(self):
        return len(self._queue) == self.max_size

    def is_empty(self):
        return len(self._queue) == 0

    def get(self, block=True):
        self._read_cond.acquire()
        if self.is_empty():
            if block:
                print("Wait for the queue to be available for reading")
                self._read_cond.wait()
            else:
                raise QueueEmpty
        data = self._queue.pop()
        self._read_cond.release()
        self._write_cond.acquire()
        self._write_cond.notify_all()
        self._write_cond.release()
        # time.sleep(0.00001)
        return data

    def put(self, data, block=False):
        self._write_cond.acquire()
        if self.is_full():
            if block:
                print("Wait for the queue to be available for writing")
                self._write_cond.wait()
            else:
                raise QueueFull
        self._queue.append(data)
        self._write_cond.release()

        self._read_cond.acquire()
        self._read_cond.notify_all()
        self._read_cond.release()
        # time.sleep(0.00001)


if __name__ == "__main__":
    import threadpool
    import threading

    queue = Queue(maxsize=10)
    threads = threadpool.ThreadPool(1)


    def wait_request_to_process():
        thread_id = threading.current_thread().ident
        print("The worker {} is ready ... ...".format(thread_id))
        while True:
            data = queue.get(block=True)
            print("{} output: {}".format(thread_id, data))


    for t in range(1):
        request = threadpool.WorkRequest(callable_=wait_request_to_process)
        threads.putRequest(request)

    import random
    import time

    while True:
        d = random.randint(1, 10000)
        try:
            queue.put(d, block=True)
        except:
            pass
        time.sleep(0.01)




