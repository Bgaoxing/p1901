#数据类型
#str
#定义：引号（单引号 ，双引号 ，三引号 ，三双引号）
#区分；其他部分编程语言会认为单引号好代表字符
#c语言中
# char c ='c'
#char * s = 'string'
s = 'hello'
s1 = "hello"
s2 = """hello"""
#转义字符
print('\n')
#原字符串  r R
print('r\n')
print('hello', end='2')
print('正方形边长：4\n 面积： 4 * 4')

#字符串拼接
# 使用+，必须为str
s1 = 'zhangs'
s2 = 'lisi'
s3 = s1 + s2
print(s3)

name = 'zhangsan'
age = 10
lession = 'python'

print('我叫张三，19岁，python')
print('我叫' + name)
print('今年' + str(age) + '岁')
print('学习'  + lession)
print('我叫' + name + '今年' + str(age) +'学习'  + lession)

# 2 格式化输出 %
print('我叫%s,今年%d岁，学习%s' % (name,age,lession))

# 3 format  推荐使用
des = '我叫{},今年{}岁，学习{}'.format(name,age,lession)
print(des)

# 详细使用format
# {数字：特殊限制}
# {} 数据依次放入占位地方
# {数字} 选取数字对应的数据填充
des = '我叫{0},今年{0}岁，学习{0}'.format(name,age,lession)
print(des)

# {:对齐方式}
# {:填充字符>列宽}
# > < ^
print('{:*>10}'.format('hello')) # 左填充
print('{:*<10}'.format('hello')) # 右填充
print('{:*^11}'.format('hello')) # 居中

# {:.数字f}
print('{:.2f}'.format(1.934455))  #取几位小数
# 思考 其他数字限定

# 二进制 八进制 十进制 十六进制

print('=' * 22,'input:')

# input
# name = input('请输入名字:')
# print('您刚输入的名字为:', name)
# print(type(name))

#备注
# input输入的数据需要接收
# input输入的数据是类型str

# 输入半径 显示圆周长及面积
# r = float(input('您输入的半径为:'))
# pi = 3.14

# print('周长为:',2 * pi * r)
# print('面积为:',3.14 * r ** 2)

# 输入商品单价和数量，求总额
# price = float(input('输入单价：'))
# number = float(input('数量：'))
# print('总额:',price * number)

# 思考 input录入多个数据，并提取使用
# 提示 tuple  eval()  或者str分割



# 二进制 八进制 十进制 十六进制
n = 99
n1 = 0b1011
print(n1)
n2 = 11
print('{:b}'.format(n2))
n3 = 23
print('{:o}'.format(n3))
print('{:x}'.format(n3))
print('{:x}'.format(30))
n4 = 0x8746
print(n4)


name = 'zs'
age = 20
lession = 'python'
print('我叫' + name + '今年' + str(age) + '课程' + lession)
print('我叫{},今年{},课程{}'.format(name,age,lession))
print('我叫{2},今年{2},课程{2}'.format(name,age,lession))
print('我叫',end=name)
print('今年' + str(age))
print('我叫\n' + name)
print('今年' + str(age))

print('{:*>20}'.format('@'))
print('{:*<20}'.format('@'))
print('{:*^20}'.format('@'))
print('{:.4f}'.format(1.234567))
# s = input('输入')
# print('刚刚输入的是' + s)

n1 = 0b10010
print(n1)
n2 = 18
print('{:b}'.format(n2))
n3 = 109
print('{:o}'.format(n3))
n4 = 0o155
print(n4)
n5 = 2768
print('{:x}'.format(n5))
n6 = 0xad0
print(n6)



# > < >= <= == !=
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 == 1)
print(1 != 1)

print(type(1 < 2))
# 注意 ==不能用于浮点数判断
# 数据类型 bool  (True False)
# 练习 输入一个整数，判断是否为3的倍数
# n = int(input('输入一个整数：'))
# print(n % 3 == 0)

# str比较： 按照ascii表进行比较
# 遇到第一个不同的字符，结束比较
s = 'aza'
s1 = 'abz'
print(s > s1)

# bool比较
print(True + 1)
print(True > 1)

# 备注 关系运算符 计算结果为bool类型

# 逻辑运算符 and  or  not
# and
print(1 < 2 and 3 < 4)
print(1 < 2 and 3 < 2)
# 结论 逻辑与运算符
# 表达式1  and  表达式2
# 一个false即为false
# 同时为true才为true

# 惰性原则
print(1 > 2 and x > 1)  # 左边执行错误就不会继续执行

#  or
print(1 < 2 or 4 < 3 )
print(1 > 2 or 2 > 3)
# 一真为真，同假则假

#  not
#  单元运算符（单目运算符）

print(not 1)
print(not 1 > 2)
# 1为ture 0为false 空为false 则非空非0为true

# 输入一个100以内的正整数，查看是否含6
n = int(input('输入一个100以内的正整数'))
print(n % 10 == 6 or n // 10 == 6)

# 成员运算符 in
print('h' in 'hello')
print('1' in '123456')







