# 作业：
# 1、循环录入5个数字，然后按反序输出（将一个数组中的值按逆序重新存放，
# l = []
# for i in range(5):
#     n = int(input('输入第{}个数:'.format(i + 1)))
#     l.append(n)
# # print(list(reversed(l)))
# l.reverse()
# print(l)


# # 例如原来的顺序为：8，6，5，4，1.要求改为：1，4，5，6，8输出；并将数组中的值输出）
# l = [8, 6, 5, 4, 1]
# l.pop(0)
# print(list(reversed(l)))


# 2、['12','13','33','34']，移除这个数组中包含1的字符串，提示：使用成员运算符in判定是否包含
# t = ['12','13','33','34']
# i = 0
# while i < len(t):
#     if '1' in t[i]:
#         t.pop(i)
#         i = i - 1
#     i = i + 1
# print(t)

#  filter()



# 3、找出一个数组中，输出数字小于33的元素 如数组：[11,22,33,1,6,4,88,44] 和数组 ['11','22','33','1','6','4','88','44']
# l = [11, 22, 33, 1, 6, 4, 88, 44]
# for i in l:
#     if i < 33:
#         print(i)
# t = ['11','22','33','1','6','4','88','44']
# for i in t:
#     if int(i) < 33:
#         print(i)



# 4、找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
# l1 = [1, 3, 2, 1, 2, 5]
# l2 = []
# i = 0
# for i in l1:
#     if l1.count(i) == 1:
#         l2.append(i)
#
# print(l2)


# 5、一个列表中，存放多个数字，查找这个列表中的最大值；
# t = [1, 4, 79, 98, 56, 100]
# def mymax(newl):
#     m = newl[0]
#     for v in newl:
#         if m < v:
#             m = v
#     return m
#
# print(mymax(t))
# print(max(t))

# print()  input()  eval()  ord()  chr()  sum()  max()  min()  bin()  help()  oct()  hex()  round()
#
# print(ord('A'))
# print(chr('65'))
# print(bin(9))  #二进制
# print(ord(9))  #八进制
# print(hex(9))  #十六进制
# print(round(10.9))  #四舍五入
# 6、随机产生20个100-200之间的正整数存放到数组中，并求数组中的所有元素最大值、最小值、平均值，然后将各元素的与平均值的差组成一个新列表。
# import random
# alist = random.sample(range(100,201),20) #random.sample()生成20个不相同的随机数
# print(alist)
# print(max(alist))
# print(min(alist))
# print(sum(alist) / len(alist)) #平均值

# import random
# l = []
# for i in range(20):
#     n = random.randint(100, 200)
#     l.append(n)
#
# m_max = max(l)
# m_min = min(l)
# avg = sum(l) // len(l)
#
# newl = []
# for v in l:
#     newl.append(v - avg)
# print(newl)
# 7、将字符串中的数字去掉，字母转为大写：“0go08o32d”
# string = '0go08o32d'
# l = list(string)
# i = 0
# while i < len(l):
#     if l[i] in '1234567890':
#         l.pop(i)
#         i = i - 1
#     i = i + 1
# print(''.join(l).upper())

# string = '0go08o32d'
# newstring = ''
# for s in string:
#     if s not  in '1234567890':
#         newstring = newstring + s
# print(newstring.upper())

# 思考
# 使用replace，将数字替换''


# 8、给定一个字符串，判断字符串中是否还有png，有就删除它
# string = 'dadatgpngpng'
# while 'png' in string:
#     string = string.replace('png', '')
# print(string)


# 9、aaabbccccdd输出为3a2b4c2d
# t = 'aaabccccdd'
# print(str(t.count('a')) + 'a', end='')
# print(str(t.count('b')) + 'b', end='')
# print(str(t.count('c')) + 'c', end='')
# print(str(t.count('d')) + 'd')

# string = 'aaabbccccdd'
# count = 1
# i = 0
# newstring = ''
# while i < len(string) - 1:
#     if string[i] == string[i + 1]:
#         count = count + 1
#     else:
#         print('{}{}'.format(count, string[i]))
#         newstring = newstring + '{}{}'.format(count, string[i])
#         count = 1
#     i = i + 1
# print('{}{}'.format(count, string[i]))
# newstring = newstring + '{}{}'.format(count, string[i])
# print(newstring)


# 10、写一个函数，计算任意一个身份证号对应的出生年月日和性别
# def calcode(card):
#     year = card[6: 10]
#     month = card[10: 12].lstrip('0')
#     day = card[12: 14].lstrip('0')
#     gerder = '女 ' if int(card[-2]) % 2 == 0 else '男'
#     return '{}年{}月{}日 {}'.format(year, month, day, gerder)
# card = '510234200009182455'
# print(calcode(card))
