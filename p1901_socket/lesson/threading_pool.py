# from concurrent.futures import ThreadPoolExecutor  #引用多线程池
# from threading import Lock, RLock  #引用锁
# # from  functools import partial  #偏函数 用于传参数
# from concurrent.futures import as_completed
#
# lock = RLock()
# num = 0
# counts = 1000000
# # 初始化线程并规定线程数量
# pools = ThreadPoolExecutor(max_workers=20)
#
# def add():
#
#     global num  #调用全局变量
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
# # pools.submit(partial(add, 5, 10))  #传参格式，如果用add，(5) 只能传一个参数，传多个参数用partial(add, 5, 10)
# function_list = [add, minus]   # 传参
# pools_list = list()
# for i in function_list:
#     pools_list.append(pools.submit(i))
# for i in as_completed(pools_list):
#     i.result()
# print(num)

from concurrent.futures import ThreadPoolExecutor
from threading import RLock
from concurrent.futures import as_completed
lock = RLock()
num = 0
counts = 1000000
pools = ThreadPoolExecutor(max_workers=20)
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

function_list = [add, jian]
pools_list = list()
for i in function_list:
    pools_list.append(pools.submit(i))
for i in as_completed(pools_list):
    i.result()
print(num)