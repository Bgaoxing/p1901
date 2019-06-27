# import time
# from threading import Thread
#
# def test1():
#     time.sleep(5)
#     print('test1 end')
#
# def test2():
#     time.sleep(3)
#     print('test2 end')
#
# # t1对应的子线程
# t1 = Thread(target=test1)
# t1.start()
# # t2主线程
# test2()
import time
from threading import Thread
def test1():
    time.sleep(2)
    print('test1 end')
def test2():
    time.sleep(3)
    print('test2 end')
t1 = Thread(target=test1)

t1.start()
test2()
