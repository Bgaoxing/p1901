# 函数
# print('hello world')

"""
函数定义

def 函数名(形式参数列表):
    函数体
    
注意
1 def 不能省略
2 函数名命名原则同变量名命名原则
3 参数列表可以为空 称为无参函数，但（）不能省略
4 冒号：缩进
5 函数只有在调用时才会执行

调用语法
函数名（实际参数列表）
如果参数列表为空，（）不能省略，否则不能调用函数
"""

# def getwater():
#     print('拿钱')
#     print('到商店')
#     print('挑水')
#     print('付钱')
#     print('回来')
#
# getwater()
#
# print('开心敲代码')
# print('.........')
#
# getwater()
#
# print('休息')
# print('.........')
#
# getwater()
#
# print('去吃饭')
# print('.........')

"""
形参 （形式函数），定义函数时的参数
实参  （实际参数），调用函数时候的参数

注意
1 形参一般只是变量，除非分隔符（*）。。。
2 实参是一个确定的值，可以是表达式、变量、。。。
"""
# def getwater(money):
#     print('拿{}块钱'.format(money))
#     print('到商店')
#     print('挑水')
#     print('付钱')
#     print('回来')
#
# a = 10
# getwater(a)
# getwater(10)
# getwater(100 + 0.1)

# def say(n):
#     for i in range(n):
#         print('hello world')
#
# say(10)

"""
参数间用逗号间隔
默认值参数必须在必须传递的参数后面
"""
# def getwater(money, watername='农夫山泉'):
#     print('拿{}块钱'.format(money))
#     print('到商店')
#     print('挑水',watername)
#     print('付钱')
#     print('回来')
#
#
# getwater(10, '怡宝')
# getwater(100)
# getwater(100, watername='')
# print(end='')


# 练习
# 0 - 10 的和
# 0 - 100 的和
# 0 - 1000 的和
# 0 - 50 的和

# def num(start, stop):
#     s = 0
#     for i in range(start, stop+1):
#         s = s + i
#     print(s)
#
# num(0, 100)
# num(stop=100, start=0)



"""
函数体：包含函数执行代码及返回值
1 如果有返回值，使用return进行返回
2 函数执行过程中，遇到return 函数结束
3 当没有返回值，也想提前结束返回自己，也可以使用return return后面不紧跟值就行，默认这个值为none（return none）
4 函数中没有return时，默认在函数结尾 存在return none
5 多值返回时，使用逗号隔开，默认为tuple类型
"""
# def getwater(money, watername='农夫山泉'):
#     print('拿{}块钱'.format(money))
#     print('到商店')
#     print('挑水',watername)
#     print('付钱')
#     print('回来')
#
#     return '一瓶豪华的' + watername
#
# result = getwater(100)
# print(result)




# 练习
# 0 - 10 的和 + 5
# 0 - 100 的和 / 2
# 0 - 1000 的和
# 0 - 50 的和

def num(start, stop):
    s = 0
    for i in range(start, stop+1):
        s = s + i
    return  s

result1 = num(0, 100) / 2
result2 = num(0, 10) + 5
print(result1, result2)






























