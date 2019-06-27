#  高阶函数

# def addnumbers(x, y):
#     return x + y
#
# def reducenumbers(x, y):
#     return x - y
#
# def huanghaoyu(x, y, f):
    # addnumbers(x, y)
    # reducenumbers(x, y)
    # f(x, y)


# huanghaoyu(10, 20, addnumbers)
# print(addnumbers)   # 函数记录着函数地址
# a = addnumbers   # 用一个变量记录这个函数名
#
# a(10, 20)   # 可以通过这个变量来调用这个函数
# addnumbers(10, 20)


# 作用域
# money = 100
# def func1():
#
#
#     def getmoney():
#         global money   #globals  全局找  nonlocal  函数内部找
#         money = 20
#         print('函数内', money)
#
#     def savemoney():
#         global money
#         money = 1000 + money
#         print(money)
#
#     return getmoney, savemoney
#
# f = func1()
# f[0]()
# f[1]()

# map() map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# l = [10, 20, 30, 40, 50, 60]
# result = map(lambda  x: x - 1, l)
# print(l)
# print(result)
# for i in result:
#     print(i)
#
#
# # filter 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True
# 的元素放到新列表中。(判断)
# l = [10, 20, 30, 40, 50, 60]
# print(list(filter(lambda x: x > 30, l)))


# [1,2,1,3,2,5] 找出只出现一次的数字
# l = [1,2,1,3,2,5]
# print(list(filter(lambda x: l.count(x) == 1, l)))
# l2 = ['12','13','33','34']
# # 移除这个数组中包含1的字符串，
# print(list(filter(lambda x: '1' not in x, l2)))
#
# # 找出一个数组中，输出数字小于33的元素
# l1 = [11, 22, 33, 1, 6, 4, 88, 44]
#
# print(list(filter(lambda x: x < 33, l1)))







import time

def caltime(f):
    def func1():
        t1 = time.time()
        f()
        t2 = time.time()
        print(t2 - t1)
    return func1

@caltime # 调用装饰器函数并将装饰的函数传入到参数中
def say():  # 将装饰器中装饰的函数返回，由该函数接收
            # say = func1
    print('saying')

@caltime    # caltime(mysum)
def mysum():  # mysum = func1
    s = 0
    for i in range(10):
        s = s + i
    print(s)

say()