# 参数的选取
# 参数是否需要外界传入，是否会改变

# 返回值（return）
# 是否需要返回值 1:函数内部是否有新的数据产生
#              2: 外界是否需要

# 求绝对值函数
a = 1 - 2
print(abs(a))


# class Student:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def differanceheight(self, otherstudent):
#         return abs(self.height - otherstudent.height)
#
#     def difference(self, aStu, bStu):
#         return abs(aStu.height - bStu.height)
#
#
# zhangsan = Student('张三', 190)
# lisi = Student('李四', 185)
# # 写一个函数，用来求得两个学生的身高差
#
# a = zhangsan.differanceheight(lisi)
# print(a)
#
# b = lisi.differanceheight(zhangsan)
# print(b)
#
# wanglaowu = Student('王老五', 170)
# c = wanglaowu.difference(zhangsan, lisi)
# print(c)

class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.1

    def eat(self):
        self.weight += 0.1

dog = Dog('二哈', 10)
dog.run()
print(dog.weight)


# Python元组的升级版本 -- namedtuple(具名元组)
# 因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道
# 一个元组所要表达的意义，所以在这里引入了 collections.namedtuple
# 这个工厂函数，来构造一个带字段名的元组。

import collections
Person = collections.namedtuple('Person', ['name', 'age', 'height'])
person = Person('科比', 40, 198)
print(person)


l1 = [11, 22, 33, 44, 55, 66, 77, 88]

print(l1[3::4])
print(l1[::7])


d = {'A': ['Ada', 'Ab'], 'Z':['Zhang', 'zhao']}
print(list(d.values()))

print(d.items())

# 按字母排序
d = {'A':['阿'], 'F':['冯'], 'C':['陈']}
keys = list(d.keys())
keys.sort()
for key in keys:
    print(d[key])




#
# 1、打印所有分数的等级（A、B、C、D）
# 2、打印及格与不及格
# 3、只打印及格

"""
js：
switch
case
case
default

"""

# i = 0
# while i < 10:
#     i = i + 1
#     continue

# i = 0
# while i < 5:
#     i = i + 1
#
#     j = 0
#     while j < 3:
#         j = j + 1
#         if j == 2:
#             print(i, j)
#             break



# t = ((11, 22, 33), (44, 55, 66), (77, 88, 99))
#
# i = 0
# a = 0  # 用来记录break是否产生
# while i < 3:
#     ts = t[i]  # 拿到内层元组
#     i = i + 1
#
#     j = 0
#     while j < 3:
#         print(ts[j])
#         if ts[j] == 66:
#             print('找到了')
#             a = 1
#             break
#         j = j + 1
#
#     if a == 1:
#         break

#
# t = (11, 22, 33)
#
# for v in t:
#     print(v)
#
# for i in range(len(t)):
#     print(i, t[i])
#
# for i,v in enumerate(t):
#     print(i, v)


# d = {'teachers': {
#                 'python': ['李老师', '张老师'],
#                 '测试': ['江老师', '刘老师']
#     },
#     'students': {
#         'python': ['李同学', '张同学'],
#         '测试': ['江同学', '刘同学']
#     }
#
# }
#
# teachers = d['teachers']
#
# for key in d:
#     print(d[key])
#     for v in d[key]:
#         print(v)


# def findandprinttuples(t, a=10):
#     for v in t:
#         print(v)
#
# print()
#
# findandprinttuples((11, 22), 1)


# t = (11, 22, 33)
# t2 = (44, 55, 66)
#
#
#
# for v in t2:
#     print(v)


# def func1():
#     """
#     函数用来做什么的
#     :return:
#     """
#     a = 10
#     b = a + 2
#     return b
#
# c = func1()
# print(c + 3)


# 案例，查询一个字典中存在某个value值
# 案例，筛选某个列表下的所有大于33的数、大于99的数
# 案例：去掉某个字符串中所有的数字


# def changelist(l1, n):
#     # i = 0
#     # while i < len(l1):
#     #     if l1[i] > n:
#     #         l1.pop(i)
#     #         i = i - 1
#     #     i = i + 1
#
#     i = 0
#     newl = []
#     while i < len(l1):
#         if l1[i] > n:
#             newl.append(l1[i])
#         i = i + 1
#
#     return newl
#
# l2 = changelist([11, 22, 33, 66, 0], 33)
# print(l2)



# list remove
# filter()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person('张三', 100)
# print(person)


# class Student:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def differanceheight(self, otherstudent):
#         return abs(self.height - otherstudent.height)
#
#     def difference(self, aStu, bStu):
#         return abs(aStu.height - bStu.height)
#
# zhangsan = Student('张三', 190)
# lisi = Student('李四', 185)
# # 写一个函数，用来求得两个学生的身高差
#
# a = zhangsan.differanceheight(lisi)
# print(a)
#
# b = lisi.differanceheight(zhangsan)
# print(b)
#
# wanglaowu = Student('王老五', 170)
# c = wanglaowu.difference(zhangsan, lisi)
# print(c)


# 创建一个狗类，包涵名字、体重
# 实例化一个'二哈'
# 定义一个方法，跑步
# 该方法实现功能为：每跑步一次，体重减少0.1
# 定义一个方法，吃饭
# 该方法实现功能为：每吃饭一次，体重增加0.1
class Dog:
    # 初始化方法（构造函数）
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def running(self):
        self.weight -= 0.1

    def eating(self):
        self.weight += 0.1


haer = Dog('二哈', 10)
haer.running()
print(haer.weight)
haer.eating()
print(haer.weight)



# 写一个函数，用来求一个数的绝对值
# def myabs(n):
#     if n < 0:
#         return -n
#     return n
#
# print(myabs(-10))


# 判定一个数是奇数还是偶数
# ?:
# n = int(input('输入一个数：'))
# a = '偶数' if n % 2 == 0 else '奇数'
# print(a)

# t = tuple()
# t = (11, )

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
#
# point1 = Point(11, 33)
# print(point1.x)


# l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# # 同时提取[44, 88]
# print(l1[3::4])
# # 同时提取[11, 88]
# print(l1[::7])
# print(l1)


# d = {'A': ['Ada', 'Ab'], 'Z': ['Zhang', 'zhao']}
# print(list(d.values()))
# l = list(d.values())
# l1 = []
# for values in l:
#     l1.extend(values)
#     # l1.extend(['Ada', 'Ab'])

# l = [11, 22]
# l1 = []
# l1.append(l)
# l1.extend(l)

# d = {'one': 11, 'two': 22}
# for index, key in enumerate(d):
#     print(index, key)


# d = {'A': ['Ada'],
#      'Z': ['zhang'],
#      'L': ['li']}
#
# keys = list(d.keys())
# keys.sort()
#
# for key in keys:
#     print(d[key])


# 2、
# 定义一个圆形类，已知半径，可提供计算圆形的周长和面积
# 定义一个圆环类，已知外半径和内半径，可提供计算圆环周长和面积

# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return 3.14 * self.r ** 2
#
#     def per(self):
#         return 2 * 3.14 * self.r
#
#
# class Ring:
#     def __init__(self, outside_r, inside_r):
#         self.outside = Circle(outside_r)
#         self.inside = Circle(inside_r)
#
#     def area(self):
#         return self.outside.area() - self.inside.area()
#
#     def per(self):
#         return self.outside.per() + self.inside.per()
#
# r1 = 3.5
# r2 = 2.5
# c1 = Circle(r1)
# print(c1.per(), c1.area())
#
# r = Ring(r1, r2)
# print(r.area())
# print(r.per())





