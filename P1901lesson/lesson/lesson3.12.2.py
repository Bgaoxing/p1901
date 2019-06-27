# import time
# # 装饰器 (将一个函数，放到另一个函数里面进行装饰并返回，输出函数本身及装饰后的值，不改变本身)
#
# def func1(temp):
#     def func2():
#         t1 = time.time()
#         temp()
#         t2 = time.time()
#         print(t2 - t1)
#     return func2
#
# @func1  # saying = func1(saying)
# def saying():
#     print('saying')
#
# # saying = func1(saying)
# saying()



# import time
# def caltime(flag):
#     def func1(temp):
#         def func2(*args, **kwargs):
#             t1 = time.time()
#             r = temp(*args, **kwargs)
#             t2 = time.time()
#
#             if flag:
#                 print(t2 - t1)
#             else:
#                 print('😊', t2 - t1)
#
#             return r
#         return func2
#     return func1
#
# @caltime(flag=True)  # saying = caltime(saying)
# def saying():
#     print('saying')
#
# @caltime(flag=False)
# def myabs(n):
#     if n < 0:
#         return -n
#     return n
#
# # saying = func1(saying)
# # saying()
# print(myabs(-1))





# 书写一个商品类：商品编号、名字、单价、数量、总额
# 总额通过单价和数量来确定，不能直接修改
# 实例化一个商品，然后打印这个商品的信息
class Goods:
    def __init__(self, idnum, name, price, number):
        self.idnum = idnum
        self.name = name
        self.price = price
        self.number = number

    @property
    def sumprice(self):
        return self.price * self.number

    def __str__(self):
        return '编号:{}, 名字:{}, 单价:{}, 数量:{}, 总价:{}' \
            .format(self.idnum, self.name,
                    self.price, self.number,
                    self.sumprice)


goods = Goods('001', 'pen', 30, 10)
print(goods)



