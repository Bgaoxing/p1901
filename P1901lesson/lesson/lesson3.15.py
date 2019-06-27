
# re.py

# import re

# string = input('输入一个字符串:')
#
# # p = 'a$'
# # p = 'a|b|c'
# # p = '[^a]'
# # p = '[a-z]'
# # p = '\d'  # \d [0-9]
# # p = '1[35]\d{9}'
#
# # p = 'a{9}'  # *  +  {}  ?
# p = '[a-zA-Z]{6,20}$'
# print(re.match(p, string))

# string = 'dafdf4567dfad567dfad78'
# p = '[a-z]'
# print(re.split(p, string))

# f = open('/Users/rimi/Desktop/P1901练习.txt')
# print(f.read())
#
# f.close()

# 异常处理
# try:
#     n = int(input('输入一个数字:'))
#     print(10/n)
# except ValueError as e:
#     print('ValueError', e)
#
# except ZeroDivisionError:
#     print('除数不为0')
#
# else:  # 无异常执行的语句
#     print(n)
#
# finally:  # 不管异常是否存在，都会执行的语句
#     print('over')


# KeyboardInterrupt
# KeyError
# ValueError

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


# try:
#     n = int(input('请输入数字:'))
#     if n == 2:
#         raise MyError('不能输入2')  # 手动触发
#
# except MyError as e:
#     print(e)

# n = int(input('请输入数字:'))
# # if n == 2:
# #     raise MyError('不能输入2')  # 手动触发
#
# print('hello world')

# 断言
# assert 1 > 2

# with open('/Users/rimi/Desktop/P1901练习.txt') as f:
#     print(f.read())

import xlrd, xlwt

# 1、 思考：将四个工作表中的内容，合并到一个excel中？？？
# 2、如何将一个文件夹下的所有excel合并到一个excel
# 提示：os.py

# 写入
# 第一步： 创建工作薄
newbook = xlwt.Workbook()
# 第二步： 添加工作表
newsheet = newbook.add_sheet('学生表')
# 第三步：写入内容
newsheet.write(0, 0, 'hello world')
# 第四步：保存
newbook.save('学生通讯录.xls')

# 读取

# # 第一步：打开工作薄
# book = xlrd.open_workbook('/Users/rimi/Desktop/studentsbooks.xlsx')
# # 如果excel表跟当前py文件同目录，则不需要书写路径
# # 直接输入文件名就可以了
#
# # 第二步：打开工作表
# sheet = book.sheet_by_index(0)
# # sheet = book.sheet_by_name('sheet名称')
# # sheetnames = book.sheet_names()
#
# # 第三步，得到整行、或者整列、或者一个cell的数据
# print(sheet.row(0))
# print(sheet.row_values(0))
# print(sheet.row_types(0))
#
# # 得到行数
# print(sheet.nrows)
# print(sheet.ncols)



