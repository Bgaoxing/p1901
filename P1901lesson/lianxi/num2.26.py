# 1、已知一个圆半径为3.5，声明一个变量名为radius存储该圆半径，要求输出该圆的半径、周长和面积，输出格式如下：
# radius = float(input('请输入半径:'))
# pi = 3.14
# print('半径为',radius)
# print('周长为',2 * pi *radius)
# print('面积为',pi * radius ** 2)
pi = 3.14
radius = 3.5
print('半径为:',radius)
print('周长:{}\n面积:{}'.format(2 * pi * radius ,pi * radius ** 2))

# 	 该圆半径为：xx
# 	 该圆周长为：xx
# 	 该圆面积为：xx


# 如果想提升优先级，可使用小括号
# 2、解释以下程序的打印结果
print(1 + 10 * 2 / 2 - 5)
print(3.0 / 5)
print(3.0 // 5)
print('a' * 10)
print(True + 3)
print(False + 3)
print('hello' > 'world')
# print('h' > 1)  字符串不能和数字比较


# 3、说出以下正确的定义变量有哪些？
# ab = 10
# *a = 20
# _a = 20
# pass = 1
# global = 2
# 1a = "hello"
# b = '''world'''
# python = ""hi""

import keyword
print(keyword.kwlist)

# 提升：
# 4：输入一个年份，得出是否为闰年
# 能够被4整除，但不能被一百整除
# 或者能够被四百整除
# year = int(input('请输入一个年份：'))
# print('是否为闰年:',year % 4 == 0 and year % 100 != 0 or != year % 400 == 0)


# 通过使用if相关语法，用来判断输入一个人年龄，打印该人是否是成年人

age = int(input('请输入年龄:'))
if age >= 18:
    print("成年人")
else:
    print("未成年")