# 9
# def str(text):
#     out = []
#     string = list(text)
#     for i in string:
#         if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#             out.append(i)
#     print("".join(out))
#
# str('This website for losers LOL')



# # 10
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, gender, age, score):
#         super().__init__(name, gender, age)
#         self.score = score
#
#     def __str__(self):
#         list.append(self.score)
#         return '{}'.format(self.score)
#
#
# class Teacher(Person):
#     def __init__(self, name, gender, age, money):
#         super().__init__(name, gender, age)
#         self.money = money
#     def __str__(self):
#         list.append(self.money)
#         return '{}'.format(self.money)
#
# list = []
# student1 = Student('zs', '男', 17, 50)
# student2 = Student('ls', '男', 16, 60)
# student3 = Student('ww', '男', 17, 70)
# student4 = Student('zl', '男', 18, 80)
# student5 = Student('cq', '男', 20, 90)
# print(student1, student2, student3, student4, student5)
#
# teacher1 = Teacher('qw', '男', 30, 60)
# teacher2 = Teacher('we', '男', 27, 70)
# teacher3 = Teacher('re', '男', 27, 80)
# teacher4 = Teacher('za', '男', 37, 90)
# teacher5 = Teacher('xa', '男', 30, 100)
# print(teacher1, teacher2, teacher3, teacher4, teacher5)
# print(list)
#
#
# s = 0
# s1 = 0
# for i in list[0: 5]:
#     s = s + i
# for i in list[5: 10]:
#     s1 = s1 + i
# print('学生总分数{}, 老师总薪资{}'.format(s, s1))




# # 11
# n = 1
# for i in range(1, 10):
#     n = (n + 1) * 2
#
# print('第1天共摘了{}个桃子'.format(n))




# 12
# class User:
#     def __init__(self, name, phone, money):
#         self.name = name
#         self.phone = phone
#         self.money = money
#     def __str__(self):
#         return '姓名:{},电话号码:{},卡内余额:{}'.format(
#             self.name, self.phone, self.money)
#
#
# class Salesman:
#     def __init__(self, name):
#         self.name = name
#
#     def inputmenu(self):
#         return int(input('选择菜单:'))
#
#     def s_adduser(self, computer):
#         import re
#         phone = input('输入用户电话号码:')
#         if len(phone) == 11 and re.match(r'1\d{10}', phone):
#             return phone
#         else:
#             print('请输入11位的手机号')
#         user = computer.searchuser(phone)
#         if user is not None:
#             return user
#         else:
#             name = input('输入用户姓名:')
#             phone = input('输入用户电话号码:')
#             money = int(input('请输入存储金额:'))
#             if money < 1000:
#                 print('存储金额不足1000，无法存储')
#             else:
#                 print('存储成功，祝您消费愉快')
#             newuser = User(name, phone, money)
#             return newuser
#
#     def s_removeuser(self, computer):
#         phone = input('输入用户电话号码:')
#         result = computer.searchuser(phone)
#         if result is not None:
#             return result
#
#
#
#
# class Computer:
#     def __init__(self):
#         self.salesman = None
#
#     users = []
#
#     def showmenu(self):
#         print('1、添加用户')
#         print('2、注销用户')
#         print('3、查看用户信息')
#         print('4、退出')
#         n = int(input('请输入菜单:'))
#         return n
#
#     def adduser(self):
#         result = self.seller.s_adduser(self)
#
#         if isinstance(result, User):
#             self.users.append(result)
#             print('新增成功')
#
#
#     def removeuser(self):
#         result = self.seller.s_adduser(self)
#         if result is not None:
#             user = result
#             self.users.remove(user)
#             print('删除成功')
#
#     def showuser(self):
#         print('*' * 10, '用户信息如下:')
#         for user in self.users:
#             if user == 0:
#                 continue
#             print('{}'.format(user))
#
#     def searchuser(self, phone):
#         for user in self.users:
#             if user.phone == phone:
#                 return user
#         print('没找到')
#
#     def start(self, seller):
#         self.seller = seller
#
#         while True:
#             n = self.showmenu()
#             pass
#             if n == 1:
#                 self.adduser()
#             elif n == 2:
#                 self.removeuser()
#             elif n == 3:
#                 self.showuser()
#             elif n == 4:
#                 break
#
#
# if __name__ == '__main__':
#     zhangsan = Salesman('张三')
#     computer1 = Computer()
#     computer1.start(zhangsan)










