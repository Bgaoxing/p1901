
# 面向对象
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#            泛指一批事物（对象的抽象画）
# 对象：一个具体的事物（类的实例化）
"""

注意：
1 类名书写同变量书写，但首字母大写（区分于系统类名）
"""

# class Person:
#     def __init__(self, name, age, gender):
#         print(self)
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def eating(self):
#         print('{}吃饭'.format(self.name))
#
#     def running(self):
#         print('跑步')
#
# # 实例化对象：类名（）
# zs = Person('张三', 10, '男')
# print(zs)
# zs.eating()
#
# ls = Person('李四', 12, '男')
# print(ls)
# ls.eating()
# ls.running()


# 案例
# # 书写一个老师类，初始化数据有姓名和年龄
# # 老师喜欢吃饭
# # 有的老师喜欢代码
# # 但都有爱好

# class Teacher:
#     def __init__(self, name, age):
#         print(self)
#         self.name = name
#         self.age = age
#     def eating(self):
#         print('{}喜欢吃饭'.format(self.name))
#     def daima(self):
#         print('代码')
#
# lteacher = Teacher('李老师', 20)
# print(lteacher)
# lteacher.eating()
# zteacher = Teacher('张老师', 30)
# print(lteacher)
# zteacher.daima()


# 方法二
class Teacher:
    def __init__(self, name, age):
        print(self)
        self.name = name
        self.age = age

    def favourite(self, i):
        print('爱好', i)
teacher = Teacher('li', 20)
teacher.favourite('打球')

# 场景
# 定义一个老师类，拥有姓名、年龄、授课内容
# 拥有 点名 方法
# 定义一个学生类，拥有姓名、年龄、性别、电话号
# 拥有 自我介绍 方法

# 实例化一个老师、一个学生，并让老师调用点名方法

class Teacher:
    def __init__(self, name, age, lesson):
        self.name = name
        self.age = age
        self.lesson = lesson

    def callname(self, student):
        print('点名', student.name)
        student.introduce()


class Student:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def introduce(self):
        print('{},{},{},{}'
              .format(self.name, self.age
                      , self.gender, self.phone))


teacher1 = Teacher('lwy', 40, 'python')
student1 = Student('zhangsan', 20, 'nan', '110')
student2 = Student('lisi', 20, 'nan', '110')

teacher1.callname(student2)
teacher1.callname(student1)