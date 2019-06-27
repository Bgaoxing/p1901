class Good:
    def __init__(self, code, name, price, number):
        self.code = code
        self.name = name
        self._price = 0
        self.price = price
        self.number = number

    @property
    def sumprice(self):
        return self.price * self.number

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if newprice < 0:
            newprice = 0

        self._price = newprice


    def __str__(self):
        return '编号:{}, 名字:{}, 单价:{}, 数量:{}, 总价:{}'\
            .format(self.code, self.name,
                    self.price, self.number,
                    self.sumprice)


good1 = Good('101', '方便面', 10, 20)
print(good1)

price = int(input('输入商品单价:'))
# if price < 0:
#     price = 0

good1.price = price
print(good1)

good2 = Good('102', '方便面', 10, 20)
newprice = int(input('输入商品单价:'))
# if newprice < 0:
#     newprice = 0
good2.price = newprice
print(good2)


class Good:
    def __init__(self, price):
        self._price = 0  # 新增一个_price的字段
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            price = 0

        self._price = price

    def des(self):
        print('描述')

    def __str__(self):
        return str(self.price)


good1 = Good(100)
good1.price = 1000
print(good1.price)

print(dir(Good))
print(dir(good1))




# # 类限制
# class Person:
#     __slots__ = ['name', '_age']
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('吃饭')
# person = Person('张三')
# person.eat()



# class Teacher:
#     books = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def buybook(self, bookname):
#         self.books.append(bookname)
#
#
# lwy = Teacher('lwy')
# lwy.buybook('C')
# print(lwy.books)
#
# xiasisi = Teacher('xiasisi')
# xiasisi.buybook('python')
# print(xiasisi.books)
# print(lwy.books)
#
# print(dir(Teacher))
# print(dir(xiasisi))


# 创建一个老师类、学生类
# 学生有姓名和电话号
# 老师可以录入学生信息，学生信息手动输入
# 老师可以删除学生信息
# 每个老师都可以重复上述行为

class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return '姓名:{}, 电话:{}'.format(
            self.name,
            self.phone
        )

class Teacher:
    students = []

    def addstudent(self):
        name = input('输入学生名字:')
        phone = input('输入学生电话号:')

        # 形成一个学生
        student = Student(name, phone)
        # 加入到学生列表下
        self.students.append(student)

    def deletestudent(self):
        pass

    def startinput(self):
        while True:
            print('1、添加学生')
            print('2、删除学生')
            print('3、显示学生')
            print('4、退出')
            n = int(input('请选择:'))
            if n == 1:
                self.addstudent()
            elif n == 2:
                self.deletestudent()
            elif n == 3:
                for stu in self.students:
                    print(stu)
            elif n == 4:
                break
        print('录入结束')


if __name__ == '__main__':
    lwy = Teacher()
    lwy.startinput()

    # xiasisi = Teacher()
    # xiasisi.startinput()