# 作业：
# 1、编写一个学校教学管理系统，学校中有教师、学生、教务、领导等角色；
# 教师：特性（姓名、年龄、性别、身份证号、授课内容）、行为（授课、吃饭）
# 学生：特性（姓名、年龄、性别、学号、所学内容、爱好）、行为（学习、玩、吃饭）
# 教务：特性（姓名、年龄、性别、所属班级）、行为（抓学习、吃饭、睡觉）
# 领导：特性（姓名、年龄、性别）、行为（专说口头禅、开会、吃饭、打麻将）
# 要求：分析题意，为他们找一个父类，创建各个对象及完成初始化方法，并调用各自的行为；
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def eat(self):
#         print('吃饭')
#
# class Teacher(Person):
#     def __init__(self, name, age, gender, code, lesson):
#         super().__init__(name, age, gender)
#         self.code = code
#         self.lesson = lesson
#     def teach(self):
#         print('授课')
#
# class Student(Person):
#     def __init__(self, name, age, gender, idcode, subjects, hobby):
#         super().__init__(name, age, gender)
#         self.idcode = idcode
#         self.subjects = subjects
#         self.hobby = hobby
#     def learn(self):
#         print('学习')
#     def play(self):
#         print('玩耍')
#
# class Jiaowu(Person):
#     def __init__(self, name, age, gender, iclass):
#         super().__init__(name, age, gender)
#         self.iclass = iclass
#     def supervision(self):
#         print('监督学习')
#     def sleep(self):
#         print('睡觉')
#
# class Leadership(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#     def koutouchan(self):
#         print('口头禅')
#     def kaihui(self):
#         print('开会')
#     def majiang(self):
#         print('打麻将')
#
#
# teacher = Teacher('李老师', 20, '男', '510199909082455','c')
# teacher.teach()
# teacher.eat()
#
# student = Student('张三', 15, '男', '001', '语文', '打篮球')
# student.learn()
# student.play()
# student.eat()
#
# jiaowu = Jiaowu('李主任', 30, '男', 'python1901')
# jiaowu.sleep()
# jiaowu.supervision()
# jiaowu.eat()
#
# leadership = Leadership('王校长', 40, '男')
# leadership.koutouchan()
# leadership.kaihui()
# leadership.majiang()
# leadership.eat()




# 2、写1个项目经理类.
# 属性: 姓名、 基本工资、项目分红(默认10000)、项目奖金.
# 行为: 介绍自己的方法.叫xx
# 每月薪水是多少.
#
# 再写1个软件工程师类.
# 属性: 姓名、基本工资、项目奖金.
# 行为: 介绍自己的方法.叫xx
# 每月薪水是多少.
# class Person:
#     def __init__(self, name, wage, bonus):
#         self.name = name
#         self.wage = wage
#         self.bonus = bonus
#     def introduce(self):
#         print('我叫{},每月工资{}'.format(self.name, self.wage + self.bonus))
#
# class Manager(Person):
#     def __init__(self, name, wage, bonus, fenhong = 10000):
#         super().__init__(name, wage, bonus)
#         self.fenhong = fenhong
#     def __str__(self):
#         return '我叫{},每月工资{}'.format(self.name, self.wage + self.bonus + self.fenhong)
#
# class Engineer(Person):
#
#
#     def __str__(self):
#         return '我叫{},每月工资{}'.format(self.name, self.wage + self.bonus)
#
# manager = Manager('李四', 10000, 5000)
# print(manager)
# engineer = Engineer('王五', 8000, 3000)
# print(engineer)



# 3、设计一个”狗“类，包含属性（颜色、奔跑的速度m / s、性别、体重kg）
# 行为： 吃：(每吃一次，体重增加0.5kg，输出吃完后的体重)  、吠（叫）：（输出所有的属性）、跑：（每跑一次，体重减少0
# .5
# kg，输出速度和跑完后的体重）
# 设计一个
# "猫"
# 类，包含属性（颜色、性别、体重）
# 行为：*吠（叫）：输出所有的属性
# 1）根据上诉内容，提炼父类，派生子类
# 2）创建对象，调用狗的吃行为和跑行为
class Animal:
    def __init__(self, weight, gender, color):
        self.weight = weight
        self.gender = gender
        self.color = color
    def call(self):
        print('吠叫')

class Dog(Animal):
    def __init__(self, weight, gender, color, speed):
        super().__init__(weight, gender, color)
        self.speed = speed
    def eat(self):
        self.weight += 0.5
    def run(self):
        self.weight -= 0.5

    def speed1(self):
        print('速度{}'.format(self.speed))

class Cat(Animal):
    pass

dog = Dog(10, '雌', '黑' ,20)
dog.call()
dog.speed1()
dog.run()
print(dog.weight)
cat = Cat(10, '雄', '白')
cat.call()



#
# 4、编写游戏相关类：
# # 1). 怪物类：当前生命值，原始生命值，当前位置，原始位置，攻击力，防御力，移动行为，攻击英雄行为，逃跑行为
# # 2). 英雄类：角色名称，等级，经验，当前生命值，原始生命值，当前位置，原始位置，移动行为，攻击怪物行为
# # 3）游戏类：将英雄和怪物传入到游戏类中，进行简单的攻击过程
# # 抽出父类，对以上编写的类进行实例化，并且赋值然后调用他们的方法
# class Role:
#     def __init__(self, alife, blife, alocation, blocation,):
#         self.alife = alife
#         self.blife = blife
#         self.alocation = alocation
#         self.blocation = blocation
#     def yidong(self):
#         print('移动')
#
# class Monster(Role):
#     def __init__(self, alife, blife, alocation, blocation, attack, defense):
#         super().__init__(alife, blife, alocation, blocation)
#         self.attack = attack
#         self.defense = defense
#     def gongji(self):
#         print('攻击英雄')
#     def run(self):
#         print('逃跑')
#
# class Hero(Role):
#     def __init__(self, alife, blife, alocation, blocation, name, level, experience):
#         super().__init__(alife, blife, alocation, blocation)
#         self.name = name
#         self.level = level
#         self.experience = experience
#     def gongji1(self):
#         print('攻击怪物')
#
# monster = Monster(1000, 2000, '李庄', '王庄', 1000, 1500)
# monster.yidong()
# monster.gongji()
# monster.run()
# hero = Hero('瓦妮莎', 50, 100000, 2000, 3000, 'a门', 'b门')
# hero.yidong()
# hero.gongji1()



# 5、建立一个学生类，增加姓名，年龄，身份证号3个属性；
# 1）给学生类增加一个birthday的只读属性，其设置方式为，在设置身份证号属性的同时设置出生日期(显示格式为2000年1月1日)；
# 2）给学生类增加一个point属性，描述学生的座位在几行几列，并计算任意2名学生的距离（假定前后左右相邻的2名同学相拒全部为1米）。
class Student:
    def __init__(self, name, age, code, point):
        self.name = name
        self.age = age
        self.code = code
        self.point = point

    def distance(self, student1):
         return ((self.point[0] - student1.point[0]) ** 2 + (self.point[1] - student1.point[1]) ** 2) ** 0.5

    @property
    def birthday(self):
        return '{}年{}月{}日'.format(int(self.code[6:10]), str(self.code[10:12]), int(self.code[12:14]))

student = Student('张三', 20, '511324199909172355', (1,2))
student1 =Student('李四', 22, '512324199907092123', (2,4))
print(student.birthday)
print(student.distance(student1))

