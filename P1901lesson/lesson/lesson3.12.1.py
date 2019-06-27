# 场景
#     创建一个狗类，具有体重、年龄、颜色、昵称等属性，可以进食、行走、看门等动作
#     创建一个羊类，具有身长、体重、年龄、颜色等属性，可以进食、行走等动作





# class Dog:
#     def __init__(self, name, age, weight, color):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.color = color
#     def eat(self):
#         print('进食')
#     def run(self):
#         print('行走')
#     def kanmen(self):
#         print('看门')
# dog = Dog('二哈', 2, 10, '棕色')
# dog.eat()
# dog.run()
# dog.kanmen()
#
#
# class Sheep:
#     def __init__(self, weight, height, age, color):
#         self.weight = weight
#         self.height = height
#         self.color = color
#         self.age = age
#
#     def eat(self):
#         print('进食')
#     def run(self):
#         print('行走')
#
# sheep = Sheep('小山', 100, 5, '白色')
# sheep.eat()
# sheep.run()


# class Animal:
#     def __init__(self, weight, age, color):
#         self.weight = weight
#         self.age = age
#         self.color = color
#     def eat(self):
#         print('进食')
#     def run(self):
#         print('行走')
#
# class Dog(Animal):
#     def __init__(self, name, age, weight, color):
#         super().__init__(weight, age, color)
#         self.name = name
#
#
#     def kanmen(self):
#         print('看门')
# dog = Dog('二哈', 2, 10, '棕色')
# dog.eat()
# dog.run()
# dog.kanmen()
#
# class Sheep(Animal):
#     def __init__(self, weight, height, age, color):
#         super().__init__(weight, age, color)
#         self.height = height
#
# sheep = Sheep('小山', 100, 5, '白色')
# sheep.eat()
# sheep.run()



# 创建一个老师类，姓名、身份证号、地址、授课内容
# 老师可以授课、吃饭

# 创建一个工程师类，姓名、身份证号、地址、开发的语言
# 工程师可以做研发、吃饭

# class Person:
#     def __init__(self, name, code, location):
#         self.name = name
#         self.code = code
#         self.location = location
#
#     def eatting(self):
#         print('吃饭')
#
# class Teacher(Person):
#     def __init__(self, name, code, location, lesson):
#         super().__init__(name, code, location)
#         self.lesson = lesson
#     def teaching(self):
#         print('授课')
#
# class Engineer(Person):
#     def __init__(self, name, code, location, language):
#         super().__init__(name, code, location)
#         self.language = language
#     def kaifa(self):
#         print('研发')
#
# teacher = Teacher('李老师', 3242336577, '成都', '语文')
# teacher.eatting()
# teacher.teaching()
#
# engineer = Engineer('王五', 3567456574, '上海', 'python')
# engineer.eatting()
# engineer.kaifa()





class Person:
    def __init__(self, name, code, address, **kwargs):
        self.name = name
        self.code = code
        self.address = address

    def eat(self):
        print('eat')


class Teacher(Person):
    def __init__(self, name, code, address, **kwargs):
        super().__init__(name, code, address, **kwargs)
        self.teachclass = kwargs.get('teachclass')

    def teach(self):
        print('teach')


class Engineer(Person):
    def __init__(self, name, code, address, **kwargs):
        super().__init__(name, code, address)
        self.creatlanguage = kwargs.get('creatlanguage')

    def creat(self):
        print('creat')

# 创建一个自由职业人员类，姓名、身份证号、地址
# 自由职业人员可以授课、做研发、吃饭, 旅游
class Free(Teacher, Engineer):
    pass


"""
1 什么事OOP，什么事OO? 什么事OOA
2 python 是多继承还是单继承
3 什么是单继承，什么是多继承
4 面向对象三大特性
5 方法重写，方法重载
"""

