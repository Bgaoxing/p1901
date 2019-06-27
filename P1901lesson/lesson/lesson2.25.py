1+1
print(1+1)
print(234+123)
print(234+123+2)
print(234+123+1)
# 变量 在程序之行过程中 值会改变
n = 234+123
print(n)
n = 10
print(n)

# 注意事项
# 变量名命名规则：
# 1 由字母 数字 下划线组成 且不能以数字开头 尽量只在特殊时候将下划线作为开头
# 2 不和系统名字重名
# 3 见名如意 首字母小写（驼峰原则。。。）
# 4 变量必须先定义 再使用

# 1a=10  错误 数字不能开头
# print=1  错误的，print系统内置函数名
# print(1)  1(1)

a = 10
print(a)
age = 10
print(age)

# 数据 ：数据类型？？？
print(type(age))
print(type(10))

# int 整型：十进制、二进制、八进制、十六进制
#  float 小数 （浮点型）
# str 字符串
print(type(1.1))
a = 10
a = 1.1


# int
# 操作：是要运算符
# + - * /
a = 10
b = 20

print(a + b, 10 + 20, b - a, b * a,a / b)
print(3 / 2)



# ** //
print(3 // 2)  # 取商（不要余数）1
print(3 ** 2 , 3 ** 3)  # 3的多次方 9 27

# print('hellow' + 1)   str不能和int相加
# print('hellow' * 10)  str * int 代表量

print('=' * 20,'华丽的分割线')

# %  (特例 了解即可，针对负数)
print(5 % 2)  # 取余数  1

# 复合赋值运算符 += -= *= /= //= %=
n = 10
n += 10
print(n)  #20
n **= 2
print(n)  #400
n %= 2
print(n)  #0
n //= 2
print(n)  #0











a = 2
b = 2
c = 3
print(a + b)  #4
print(a - b)  #0
print(a * b)  #4
print(a / b)  #1
print(c // b) #1
print(c % b)  #1
a += b
print(a)      #4
a -= 1
print(a)      #3
a **= b
print(a)      #9
c //= b
print(c)      #1
c %= b
print(c)      #1

print('*' * 30)

n = 'zs'
print(n + str(10))



