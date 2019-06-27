# 作业：
# 1、
# 新创建一个Student类，该类的实例包含属性
# （姓名 name，性别gender，年龄age，身份证号code，身高height，体重）
#
# 给学生类增加一个比较2名学生身高的方法，打印最高的身高；

class Student:
    def __init__(self, name, gender, age, code, height, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.code = code
        self.height = height
        self.weight = weight

    def compare(self, i):
        if self.height > i.height:
            print('最高身高', student1.height)
        elif self.height < i.height:
            print('最高身高', student2.height)
        else:
            print('无法比较')

class Teacher:
    def __init__(self,name, age, student):
        self.name = name
        self.age = age
        self.student = student
    def compare1(self, i):

        print('年龄差', self.age - i.age)
    def asd(self,i):
        print('口头禅', i)


student1 = Student('zs', '男', 15, '510324', 160, 130)
student2 = Student('ls', '男', 16, '510123', 180, 140)
teacher = Teacher('LL', 30, Student)
teacher.compare1(student1)
teacher.compare1(student2)

student1.compare(student2)
teacher.asd('吹口哨')
#
# 新创建一个Teacher类，该类的实例包含属性：姓名、年龄、学生（Student对象）；
# 1）写一个方法：计算老师与学生年龄的差值；
# 2）添加一个老师的行为(方法)，打印输出该老师的口头禅；

# 2、
# 定义一个圆形类，已知半径，可提供计算圆形的周长和面积
# 定义一个圆环类，已知外半径和内半径，可提供计算圆环周长和面积
# class Round:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         print('面积', 3.14 * self.r ** 2)
#
#     def zhouchang(self):
#         print('周长', self.r * 3.14 * 2)
#
# round = Round(2)
# round.area()
# round.zhouchang()
#
# class Round:
#     def __init__(self, r):
#         self.r = r
#     def mianji(self, i):
#         print('面积', i.r ** 2 * 3.14 - self.r ** 2 * 3.14)
#     def zc(self, i):
#         print('周长', 3.14 * 2 * self.r + 3.14 * 2 * i.r)
#
# round1 = Round(3)
# round2 = Round(4)
# round1.mianji(round2)
# round1.zc(round2)
# 方法二：
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def per(self):
        return 2 * 3.14 * self.r


class Ring:
    def __init__(self, outside_r, inside_r):
        self.outside = Circle(outside_r)
        self.inside = Circle(inside_r)

    def area(self):
        return self.outside.area() - self.inside.area()

    def per(self):
        return self.outside.per() + self.inside.per()


r1 = 3.5
r2 = 2.5
c1 = Circle(r1)
print(c1.per(), c1.area())

r = Ring(r1, r2)
print(r.area())
print(r.per())

# 选做题：
# 编写游戏相关类：
# 1). 怪物类：当前生命值，原始生命值，当前位置，原始位置，攻击力，防御力，移动行为，攻击英雄行为，逃跑行为
# 2.) 英雄类：角色名称，等级，经验，当前生命值，原始生命值，当前位置，原始位置，移动行为，攻击怪物行为
# 对以上编写的类进行实例化，并且赋值然后调用他们的方法