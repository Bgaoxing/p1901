# if
a = 100
b = 200
print(a)
print(b)

"""
if:

if之前的语句
if 条件判断语句:
    条件判断为真需要执行的语句
if之后的语句

备注
1 冒号是英文输入
2 冒号下一行必须缩进，并必须有一条语句，如果暂时没想好语句，可用pass占位
3 if之后的语句不能缩进

"""
# 购买400以上打85折
# money = int(input('输入金额:'))
#
# if money >= 400:
#     money = money * 0.85
#
# print('实际支付{}元'.format(money))

# 练习 输入身高，显示是否需要购买儿童票
# height = int(input('输入身高(cm):'))
# if height <= 120:
#     print('儿童票')


# if - else
"""
注意
1 else后面跟冒号 （没有表达式）
2 下一行缩进
"""


# 购买400以上打85折 其他打95
# money = int(input('输入金额:'))
#
# if money >= 400:
#     money = money * 0.85
# else: #money < 400
#     money = money * 0.95
#
# print('实际支付{}元'.format(money))


"""
elif
"""
# 购买400以上打85折 其他打95 购买1000以上打75 并减50
# money = int(input('输入金额:'))
#
# if money >= 1000:
#     money = money * 0.75 - 50
# elif money >= 400:
#     money = money * 0.85
# else: #money < 400
#     money = money * 0.95
#
# print('实际支付{}元'.format(money))


# 85-100 A
# 70-84  B
# 60-69  C
# 0-59   D

# score = float(input('输入分数:'))
#
# if 85 <= score <= 100:
#     print('A')
# elif 70 <= score:
#     print('B')
# elif 60 <= score:
#     print('C')
# elif score >=0:
#     print('D')
# print('over')




#  循环
n = 0

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))
print('编号3')
n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

n = n + 1
print('编号{}'.format(n))

print('over')

"""
while  可用于死循环

while之前的语句
while 判定语句:
    条件为真需要执行的语句（重复性的代码）
    
    while之后的语句
    
注意
1 循环增量，循环条件，循环体
2 冒号，缩进
3 避免死循环
"""
# 打印编号1到10
n = 0
while n < 10:
    n = n + 1
    print('编号{}'.format(n))
print('over')

# 打印编号十到编号1

n = 10
while n > 0:
    print('编号{}'.format(n))
    n = n - 1
print('over')

# 打印1-100的偶数
# i = 0
# while i < 100:
#     i = i + 2
#
# print('1-100的偶数{}'.format(i))

# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#     n = n + 1
#
# n = 0
# while n < 5:
#     n = n + 1
#     m = int(input('输入第{}个数字'.format(n)))
# print('刚输入的数字:',m)


# 求 1-100的和
# 进阶 输入10个数字 求和

# i = 0
# s = 0
# while i < 100:
#     i = i + 1
#     s = s + i
# print(s)


# n = 0
# s = 0
# while n < 10:
#     n = n + 1
#     score = int(input('输入第{}个分数'.format(n)))
#     if score < 0:
#         n = n - 1
#     else:
#         s = s + score
# print(s)



"""
请输入语文成绩
     数学成绩
     英语
     地理
     。。。。
"""
# n = 0
# s = 0
# lessons = ('语文', '数学', '英语', '地理', '化学', '历史', '生物', '政治')
# while n < len(lessons):
#     n = n + 1
#     score = int(input('输入{}分数:'.format(lessons[n-1])))
#     if score < 0:
#         n = n - 1
#     else:
#         s = s + score
# print(s)


# tuple 元组
t = (11, 22, 33, 44, 55, 66, 77, 88)
lessons = ('语文', '数学', '英语', '地理', '化学', '历史', '生物', '政治')
print(t)
print(type(t))

# 取得元素，通过索引（下标，角标）
# 语法：元组名称[索引]
# 索引从0开始


print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[5])
print(t[6])
print(t[7])
# print(t[8])  错误 超出范围


i = 0
while i < len(t):
    print(t[i])
    i = i + 1

# 注意
# 1 只有一个元素时，逗号不能省略
# # 2 元组中的元素值不能修改（不支持）
# # 3 下标可以是负数 但注意越界问题（负数代表选取后面元素，例如题中的-1则是政治成绩88）
# # t[0] = 1  错误，元组中的元素不支持修改


# [index]
# [start : end : step=1]

t = (11, 22, 33, 44, 55, 66, 77, 88)
print(t[::])
print(t[::2])
print(t[:4])   # 右开区间，（end取不到）
print(t[2:])
print([len(t)])


# 取所有元素
print(t)
print(t[:])
print(t[::])
print(t[0:len(t)])

#  取负数 从元组后面开始选取，没有0说法
print(t[-1])
print(t[-3])









