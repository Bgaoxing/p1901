# 升级版1：添加姓名、分数


# def calscore(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#
#     # 新增了输入学生的名字
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
#         if len(s[key]) != 0:  #判断是否有分数
#             print('学科{}的成绩如下:'.format(key))
#             for stu in s[key]:
#                 print('姓名:{}, 成绩:{}'
#                       .format(stu['姓名'], stu['分数']))
#
#     print('*' * 30)
#
#
# def showstart():
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
#
# if __name__ == '__main__':
#     showstart()






# 升级版2  修改成绩


def searchstudent(key, name, scores):
    for stu in scores[key]:
        if stu['名字'] == name:
            print('学生存在')
            return stu

    print('学生不存在')


def addstudent(n, scores):

    keys = tuple(scores.keys())  # 取得所有科目
    key = keys[n - 1]
    print(key)

    name = input('输入名字:')
    # 判断该名字是否已经存在
    result = searchstudent(key, name, scores)
    if result is None:
        score = int(input('输入分数:'))

        studic = {'名字': name, '分数': score}
        scores[key].append(studic)
    else:
        print('不能重复添加，该学生分数为:', result['分数'])

    print('打印相关信息')

def editinfo(n, scores):
    keys = tuple(scores.keys())
    key = keys[n - 6]

    # 输入学生名字，查找该学生是否存在
    # 如果存在，则输入新的分数
    # 如果不存在，则不能输入
    name = input('输入学生名字:')
    result = searchstudent(key, name, scores)
    if result is None:
        print('不能修改成绩')
    else:
        score = int(input('输入新的分数:'))
        result['分数'] = score
        print('修改成功')

def showallinfo(scores):
    print('*' * 22, '所有学科成绩如下:')
    for key in scores:
        if len(scores[key]) != 0:
            print('学科{}的成绩如下:'.format(key))
            for stu in scores[key]:
                print('名字:{}, 成绩:{}'.format(stu['名字'], stu['分数']))

def showmenu():
    print('1、输入语文成绩:')
    print('2、输入数学成绩:')
    print('3、输入英语成绩:')
    print('4、显示所有成绩:')
    print('5、退出')
    print('6、修改语文下的某个人成绩')
    print('7、修改数学下的某个人成绩')
    print('8、修改英语下的某个人成绩')

    return int(input('请选择菜单:'))

def start():

    scores = {'语文': [],
              '数学': [],
              '英语': []}


    while True:
        n = showmenu()
        if 1 <= n <= 3:
            addstudent(n, scores)
        elif n == 4:
            showallinfo(scores)
        elif n == 5:
            break
        elif 6 <= n <= 8:
            editinfo(n, scores)


if __name__ == '__main__':
    start()