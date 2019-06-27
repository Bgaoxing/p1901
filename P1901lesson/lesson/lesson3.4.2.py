# list
# l = list()
# print(l)
#
# l1 = list('112')
# print(l1)

# 增加
# l2 = [11, 22, 33]
# l2.append(44)
# print(l2)
#
# l2.insert(1, 55)
# print(l2)
#
# # 当insert 的index大于了范围，默认在末尾
# # index 如果是负数，超过了范围，则默认放在首位
# l2.insert(11, 66)
# print(l2)
# l2.insert(-11, 66)
# print(l2)
#
# l2.extend((88, 99))
# print(l2)

# 练习 依次放10个数，放入list中
# l3 = []
# for i in range(10):
#     n = int(input('输入第{}个数:'.format(i + 1)))
#     l3.append(n)
# print(l3)

# 删除
# l2 = [11, 22, 33, 44, 55, 66, 77]
# # l2.clear()
# if 1 in l2:
#     l2.remove(1) remove前提是有值
# del

# l2.pop()  #默认删除最后一个
# l2.pop(1)  # 删除第一个位置的数
# # pop： 当index超出范围或为空时，会产生异常
# print(l2)

# l2 = [11, 22, 11, 11, 33, 44, 11, 55, 66, 11]
# #删除所有11
# # while 11 in l2:
# #     l2.remove(11)
#
# i = 0
# while i < len(l2):
#     if 11 == l2[i]:
#         l2.pop(i)
#         i = i - 1
#     i = i + 1
# print(l2)


# 修改
# l2 = [11, 22, 33, 11]
# l2[0] = 1
# print(l2)


# 查询 in  count()  index()
# l2 = [11, 22, 33, 44, 11, 55]
# c = l2.count(11)
# print(c)
# i = l2.index(11)
# i = l2.index(11, 1, 3)  #范围内不存在时，产生异常
# print(i)


# temp = [11, 22, 33]
# l1 = [temp, 44, 55, 66]

# 1 如果把temp【-1】= 99
# 问 l1中会不会把33改为99
# 2 l2中会不会把33改为99
# l2 = l1.copy()
# print(l1)
# print(l2)
#
# import  copy
# l3 = copy.deepcopy(l1)
# temp[-1] = 99
# print(l3)

# 增
# append（）、insert（）、extend()
# 方法
#
# append（）方法：在末尾添加元素
#
# s = ['how', 'are', 'you']
# s.append('fine')
# print(s)
#
# ['how', 'are', 'you', 'fine']
#
# insert（）方法：在指定位置添加元素或者列表
#
# s = ['how', 'are', 'you']
# s.insert(3, 'fine')
# print(s)
#
# ['how', 'are', 'you', 'fine']
#
# extend（）方法：可迭代，分解成元素添加在末尾。
#
# s = ['how', 'are', 'you']
# s.extend('fine')
# print(s)
#
# ['how', 'are', 'you', 'f', 'i', 'n', 'e']
#
# 删
#
# pop()、remove（）、clear（）、del
#
# pop()
# 方法： 按照下标索引删除指定的值
#
# s = ['how', 'are', 'you']
# s.pop(0)
# print(s)
#
# ['are', 'you']
#
# remove()
# 方法：按元素删除指定的值
#
# s = ['how', 'are', 'you']
# s.remove('are')
# print(s)
#
# ['how', 'you']
#
# clear()
# 方法：清空列表内数据
#
# s = ['how', 'are', 'you']
# s.clear()
# print(s)
#
# []
#
# del：删除列表、也可以进行切片删除
#
# 复制代码
# 删除列表：
#
# s = ['how', 'are', 'you']
#
# del [s]
# 打印结果为空
#
# 切片删除:
# s = ['how', 'are', 'you']
# del s[0:2]
# print(s)
#
# s = ['how', 'are', 'you']
# s[1] = "old"
# print(s)
# ['how', 'old', 'you']
# 复制代码
#
# 改
#
# s[] = '  '  # 元素赋值
#
# li = [1, 2, 3, 5, 'cat', 2, 3, 4, 5, 'bye']
# li[3] = 'monkey'
#
# print(li)
#
# s[0:2] =  ‘  ’  # 分片赋值
# #
# li = [1,2,3,5,'cat',2,3,4,5,'bye']
# li[0:3]=('a')
# print(li)
#
#
# 查：查询列表可通过下标和切片的方式
#
# 复制代码
# 1.
# 下标取值索引, 从0开始
#
# names = ['mike', 'mark', 'candice', 'laular']
#
# print(names[2])
#
# candice
#
# 2.
# 切片: 顾头不顾尾, 且切片下标的操作同样用于字符串
#
# names = ['mike', 'mark', 'candice', 'laular']
#
# print(names[1:3])  # 通过切片方式取值,切片是顾头不顾尾,打印结果:['mark', 'candice']
#
# print(names[1:])  # 取下标后面所有的值,打印结果:['mark', 'candice', 'laular']
#
# print(names[:3])  # 取下标前面所有的值,打印结果:['mike', 'mark', 'candice']
#
# print(names[:])  # 取所有的值,打印结果:['mike', 'mark', 'candice', 'laular']
#
# print(names[-1])  # 取最后一个值,打印结果:laular
#
# print(names[:1:2])  # 隔几位取一次,默认不写步长为1,即隔一位取一次;结果为取下标为1之前的值,隔2位取一个['mike']
# 复制代码
# 列表其他方法
#
# 复制代码
# index()
# 方法：获取指定元素的下标
#
# s = ['how', 'are', 'you']
# s1 = s.index('are')
#
# print(s1)
# 获取的元素下标为1
# 注：列表中s.find（）不可用作获取元素的下标。
#
# count()
# 方法：计算元素出现的次数
#
# s = ['how', 'are', 'you', 'you']
# s1 = s.count('you')
# print(s1)
#
# 2
#
# sort()
# 方法：进行排序，默认是正向排序，想要反向排序需要加：（reverse = True）, reverse返转的意思
#
# 正向排序：
# s = [1, 4, 8, 5, 6, 2, 3]
# s.sort()
# print(s1)
#
# [1, 2, 3, 4, 5, 6, 8]
# 此时默认reverse = false
#
# 反向排序：
#
# 当reverse = True时，
# s = [1, 4, 8, 5, 6, 2, 3]
# s.sort(reverse=True)
# print(s)
#
# [8, 6, 5, 4, 3, 2, 1]
#
# 翻转：
#
# s = [1, 4, 8, 5, 6, 2, 3]
# s.reverse()
# print(s)
#
# [3, 2, 6, 5, 8, 4, 1]