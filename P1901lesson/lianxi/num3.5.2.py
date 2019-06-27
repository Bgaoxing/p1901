# 升级版2：

# 升级版1：添加姓名、分数
# 英语
# 'zhangsan'  100  'nan'
# 'lisi' 90

# {
#  '语文': [],
#  '数学': [],
#  '英语': [{'name':'zhangsan', 'score':100, 'gender':'nan'},
#          {'name':'lisi',      'score':90,  'gender':'nan'}]
#  }


# {
#  '语文': {},
#  '数学': {},
#  '英语': {'zhangsan': 100,
#         'lisi': 90}
#  }


# scores = {'语文': [
#     {'姓名': 'zhang', '年龄': 10, '性别': 'nan'},
#     {'姓名': 'wang', '年龄': 12, '性别': 'nan'}
#
# ]}
#
# persons = scores['语文']
#
# for per in persons:
#     print(per['姓名'], per['年龄'], per['性别'])
#
#
#
#
#
#
# exit()
# name = input('输入姓名:')
# age = int(input('输入年龄:'))
# gender = input('输入性别:')
#
# person = {'姓名': name, '年龄': age, '性别': gender}
# scores['语文'].append(person)
#
# name = input('输入姓名:')
# age = int(input('输入年龄:'))
# gender = input('输入性别:')
#
# person1 = {'姓名': name, '年龄': age, '性别': gender}
# scores['语文'].append(person1)
#


company = {
    'name': 'rimi',
    'teachers': {'测试': ['李老师', '江老师'],
                 'Python': ['胡老师'],
                 'Java': ['程老师', '张老师']},
    'students': {
        'Python': {'P1901': ['张三', '李四'],
                   'P1902': ['王老五']},
        '测试': {'C1901': ['老赵']}
    },
    'address': '成都'
}

# # 得到teachers
# teachers = company['teachers']
# # teachers是dict，通过key遍历
# for key in teachers:
#     # 通过key得到老师列表
#     teacherlist = teachers[key]
#     # 遍历老师列表
#     for teacher in teacherlist:
#         print(teacher)










# def calscore(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#
#     # 新增了输入数学的名字
#     name = input('输入学生名字:')
#     score = int(input('请输入{}成绩:'.format(key)))
#     # 新增 形成学生信息
#     student = {'姓名': name, '分数': score}
#     # 添加了学生信息
#     s[key].append(student)
#
#     # 重新设定打印信息
#     print('当前{}学科，成绩如下:'.format(key))
#     for stu in s[key]:
#         print(stu['分数'], end=' ')
#     print()
#
# def showmenu():
#     print('1、请输入语文成绩:')
#     print('2、请输入数学成绩:')
#     print('3、请输入英语成绩:')
#     print('4、查看所有成绩:')
#     print('5、退出')
#     n = int(input('请选择菜单:'))
#     return n
#
#
# def showallinfo(s):
#     print('*' * 22, '所有学科成绩如下:')
#
#     for key in s:
#         if len(s[key]) != 0:
#             print('学科{}的成绩如下:'.format(key))
#             for stu in s[key]:
#                 print('姓名:{}, 成绩:{}'
#                       .format(stu['姓名'], stu['分数']))
#
#     print('*' * 30)
#
#
# if __name__ == '__main__':
#     scores = {'语文': [], '数学': [], '英语': []}
#
#     while True:
#         n = showmenu()
#         if 1 <= n <= 3:
#             calscore(n, scores)
#         elif n == 4:
#             showallinfo(scores)
#         elif n == 5:
#             break
#

# 基础版:添加分数
# def calscore(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#
#     score = int(input('请输入{}成绩:'.format(key)))
#     s[key].append(score)
#
#     print('当前学科{}的总成绩为:{}, 所有成绩为:{}'
#           .format(key, sum(s[key]), s[key]))
#
#
# def showmenu():
#     print('1、请输入语文成绩:')
#     print('2、请输入数学成绩:')
#     print('3、请输入英语成绩:')
#     print('4、查看所有成绩:')
#     print('5、退出')
#     n = int(input('请选择菜单:'))
#     return n
#
#
# if __name__ == '__main__':
#     scores = {'语文': [], '数学': [], '英语': []}
#
#     while True:
#         n = showmenu()
#         if 1 <= n <= 3:
#             calscore(n, scores)
#         elif n == 4:
#             print(scores)
#         elif n == 5:
#             break





