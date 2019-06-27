# from threading import Thread
# from threading import Lock, RLock
# # Lock 一般的锁 （锁太多会出现死锁）
# # RLock 高级锁（不管多少锁都会解锁）
# # 线程锁
# num = 0
# # cpu实际执行了counts * 10 次
# # 操作系统会随时把你的程序'切出去'，保证你的程序不卡顿
# # 1 执行次数过多，一般是10w次
# # 2 执行时间过长
# counts = 1000000
#
# lock = RLock()  #实例化一个锁
# def add():
#     global num   #引用全局变量
#     global counts
#     for i in range(counts):
#         lock.acquire()  #加锁
#         num = num + 1
#         lock.release()  #解锁 不解锁的话就一直占位，其他程序设计也不能执行
#
# def minus():
#     global num
#     global counts
#     for i in range(counts):
#         lock.acquire()  #加锁  前提是前面的锁解除了
#         num = num - 1
#         lock.release()  #解锁
#
# s1 = Thread(target=add)
# s2 = Thread(target=minus)
# s1.start()
# s2.start()
# s1.join()
# s2.join()
# print(num)

from threading import Thread
from threading import RLock
num = 0
counts = 1000000
lock = RLock()
def add():
    global num
    global counts
    for i in range(counts):
        lock.acquire()
        num += num
        lock.release()
def jian():
    global num
    global counts
    for i in range(counts):
        lock.acquire()
        num -= num
        lock.release()
t1 = Thread(target=add)
t2 = Thread(target=jian)
t1.start()
t2.start()
t1.join()
t2.join()
print(num)