"""
练习：
学校某社团为了管理本社团成员，现开发一个社团管理系统，可进行以下操作：
1、添加成员（成员信息：编号（唯一）、姓名、年龄、电话号、地址）
1 zs 10 131.. 成都
2 ls 12 123.. 绵阳
3 ww 14 134.. 德阳
2、根据成员编号查询成员信息
3、根据成员编号修改成员信息（可修改电话号和地址）
4、可移除某个成员
5、可一次性查看所有成员信息
6、退出

提示：成员信息相同、都属于同一个社团下；
"""

# persons = []
#
# def start():
#
#     while True:
#         n = shown()
#         if n == 1:
#             addpersons()
#         # elif n == 2:
#         #     findpersons()
#         elif n == 3:
#             changepersons()
#         elif n == 4:
#             deletepersons()
#         elif n == 5:
#             showpersons()
#         elif n == 6:
#             break
#
# def shown():
#
#     print('1:添加成员（成员信息：编号（唯一）、姓名、年龄、电话号、地址）')
#     print('2:根据成员编号查询成员信息')
#     print('3:根据成员编号修改成员信息（可修改电话号和地址）')
#     print('4:可移除某个成员')
#     print('5:可一次性查看所有成员信息')
#     print('6:退出')
#
#     return int(input('请选择菜单:'))
#
# def addpersons():
#     name = input('输入新成员的名字:')
#     age = input('输入新成员的年龄:')
#     num = input('输入新成员的编号:')
#     phone = input('输入新成员电话号码')
#     address = input('输入新成员地址')
#     npersons = {}
#     npersons['name'] = name
#     npersons['age'] = age
#     npersons['num'] = num
#     npersons['phone'] = phone
#     npersons['address'] = address
#     persons.append(npersons)
#
# #
# # def findpersons():
# #     for i in persons:
# #         n = int(input('请输入成员编号:'))
# #         if n > len(persons):
# #             return
# #         else:
# #
# #             print('{} {} {} {} {}'.format(i.['name'] - 1, ['age'] - 1, ['num'] - 1,
# #                                           ['phone' - 1], ['address'] - 1))
#
#
#
# def changepersons():
#     personsnum = int(input('请输入要修改的成员序号：')) - 1
#     newphone = input('输入修改后成员的电话号码:')
#     newaddress = input('输入修改后成员的地址:')
#     persons[personsnum]['phone'] = newphone
#     persons[personsnum]['address'] = newaddress
#
#
#
#
#
# def deletepersons():
#     delNum = int(input('请输入要删除的序号：')) - 1
#     del persons[delNum]
#
#
# def showpersons():
#     print('*' * 30)
#     print('成员信息如下：')
#     print('*' * 30)
#     i = 1
#     for temppersons in persons:
#         print('{} {} {} {} {}'.format(i, temppersons['name'], temppersons['age'], temppersons['num'],
#                                   temppersons['phone'], temppersons['address']))
#         i += 1
#
#
#
# if __name__ == '__main__':
#     start()







"""
方法二

练习：
学校某社团为了管理本社团成员，现开发一个社团管理系统，可进行以下操作：
1、添加成员（成员信息：编号（唯一）、姓名、年龄、电话号、地址）
2、根据成员编号查询成员信息
3、根据成员编号修改成员信息（可修改电话号和地址）
4、可移除某个成员
5、可一次性查看所有成员信息
6、退出

提示：成员信息相同、都属于同一个社团下；
"""

"""
[
    {'编号': '1001', 姓名': 'zhangsan', '年龄': 12, '电话号': 110, '地址': 'rimi'},
    {}

]

"""


def addstudent(students):
    # 添加成员信息
    # 输入编号，根据编号查看是否已经存在
    # 如果已经存在，则提示不能重复添加
    # 如果不存在，则提示输入学生姓名等信息
    # 添加到社团中
    code = input('输入编号:')
    result = searchstudent(code, students)
    if result is not None:
        print('学生信息:', result)
        return
    name = input('输入名字:')
    age = int(input('输入年龄:'))
    phone = input('输入电话号:')
    address = input('输入地址:')

    student = {'编号': code, '姓名': name,
               '年龄': age, '电话号': phone,
               '地址': address}

    students.append(student)


def removestudent(students):
    """
    :param students: 总的社团人数
    :return: None
    1、输入编号，查看该编号是否存在，
    2、如果存在，则删除
    3、如果不存在，提示不能删除
    """
    code = input('输入编号:')
    result = searchstudent(code, students)
    if result is not None:
        students.remove(result)
        print('删除成功')
    else:
        print('不能删除不存在的成员')


def editstudent(students):
    """
    1、输入编号，查看该编号是否存在
    2、如果存在，则提示修改什么信息
    3、如果不存在，则提示不能修改
    """
    code = input('输入编号:')
    stu = searchstudent(code, students)
    if stu is None:
        print('不能修改不存在的成员:')
        return

    print('1、修改电话号')
    print('2、修改地址')
    n = int(input('请选择需要修改的信息:'))
    if n == 1:
        phone = input('输入新的电话号:')
        stu['电话号'] = phone
    elif n == 2:
        address = input('输入新的地址:')
        stu['地址'] = address
    print('修改成功')


def searchstudent(code, students):
    for student in students:
        if student['编号'] == code:
            print('学生存在')
            return student
    print('学生不存在')


def showallinfo():
    pass


def showoneinfo():
    pass


def showmenu():
    print('1、添加成员:')
    print('2、查询某个成员')
    print('3、删除成员')
    print('4、修改成员信息')
    print('5、查看所有成员')
    print('6、退出')
    n = int(input('请选择菜单:'))
    return n


if __name__ == '__main__':
    students = []
    while True:

        n = showmenu()
        if n == 1:
            addstudent(students)
        elif n == 3:
            removestudent(students)
        elif n == 4:
            editstudent(students)
        elif n == 5:
            print(students)
        elif n == 6:
            break