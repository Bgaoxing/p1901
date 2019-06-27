# set  自学
# dict

# dict = {'name': 'zhangsan',
#         'age': 30}

# 1 字典定义：字典是以键值对形式存储
# 2 键值对必须成对出现 （key：value）
# 3 键值对之间使用逗号分隔，一个键值对是一个字典中的元素
# 4 key不能重复，key尽量是str，不能变
# 5 字典通过key取值

#取值
d = {'one': 1, 'two': 2}
# print(d['one'])
# # print(d['three'])  # key 不存在时，产生异常
#
# print(d.get('three'))  # key 不存在时，返回None
# print(d.get('one'))
#
for key in d:
    print(key, d[key])

print(list(d))  # 只能拿到key组成的list
# print(d.keys())
#
for key in d.keys():
    print(key, d[key])
#
# for value in d.values():
#     print(value)

# d = {'number': [11, 22, 33],
#      'name': 'zhangsan',
#      'status': ((200, 'success'), (404, 'notfound'))}
# # 取得33
#
# print(d['number'][-1])


# company = {
#     'name': 'rimi',
#     'teachers': {'测试': ['李老师', '江老师'],
#                  'Python': ['胡老师'],
#                  'Java': ['程老师', '张老师']},
#     'students': {
#         'Python': {'P1901': ['张三', '李四'],
#                    'P1902': ['王老五']},
#         '测试': {'C1901': ['老赵']}
#     },
#     'address': '成都'
# }
#
# print(company['teachers']['测试'][0])
# print(company['students']['测试']['C1901'])



# d = {'one': 1, 'two': 2}
#
# student = {'name': 'zhangsan', 'age': 10}
# student1 = {'name': 'lisi', 'age': 20}
# student2 = {'name': 'wangwu', 'age': 30}
# l = [student, student1, student2]
# #  求年龄之和
# s = 0
# for stu in l:
#     print(stu['age'])
#     s = s + stu['age']
# print(s)


# students = []
# while True:
#     print('1 输入学生:')
#     print('2 显示所有年龄和:')
#     print('3 结束:')
#
#     n = int(input('请选择:'))
#     if n == 1:
#         name = input('输入姓名:')
#         age = int(input('输入年龄:'))
#         student = {'name': name,
#                    'age':age}
#         students.append(student)
#     elif n == 2:
#         print(students)
#     elif n == 3:
#         break




# scores = [11, 22, 33, 44, 77, 8, 99, 67, 89]
# #A B C D
# scoredic = {'A':[], 'B':[], 'C':[], 'D':[]}
# for score in scores:
#     if score >= 90:
#         scoredic['A'].append(score)
#     elif  75 <= score < 90:
#         scoredic['B'].append(score)
#     elif  60 <= score <75:
#         scoredic['C'].append(score)
#     else:
#         scoredic['D'].append(score)
#
# print(scoredic)


# 数据与函数
# def changenumber(n):
#     n = 0
#     print(n)
#
# x = [11, 22]
# changenumber(x)
# print(x)


# dic其他函数
# 删除（清空）
# d = {'one': 1, 'two': 2}
# d.clear()

#遍历每个元素
# print(d.items())
# for k, v in d.items():
#     print(k, v)

#删除元素
# d.pop('one')
# print(d.popitem())    #当dict空，产生异常
# print(d)

#添加
# d.setdefault('one', 111)
# d.setdefault('three', 333)   #key存在，添加
# print(d)

# d = {'one': 1, 'two': 2}
# d['one'] = 11  #当key存在，修改操作
# d['three'] = 3  #当key不存在，添加操作
# print(d)


# 查询
# print(11 in d)

# 新增遍历方式  按下标遍历
# l = [11, 22, 33]
# for v in enumerate(l):
#     print(v)



# def func1(a, b, c=1, d=2, **kwargs):
#     print(a, b, c, d, kwargs)
#
# func1(1, 2, 3, 4, name='zhang', age=10)

# def saveinfo(**kwargs):
#     print(kwargs)
#
# saveinfo(name='zhangsan', age=10)
# studic = {'one': 11}
# saveinfo(**studic)


# def func1(a, b, *, c, d):
#     print(a, b, c, d)
#
# func1(1, 2, c=3, d=4)