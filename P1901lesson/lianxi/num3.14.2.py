class Student:
    def __init__(self, code, name, age, score):
        self.name = name
        self.age = age
        self.code = code
        self.score = score

    def __str__(self):
        return '学号:{},姓名:{},年龄:{}, 分数:{}'.format(
            self.code, self.name,
            self.age, self.score
        )


class Teacher:
    def __init__(self, code, name):
        self.name = name
        self.code = code

    def te_addstudent(self, computer):
        """
        1、输入学生编号;
        2、计算机查找是否存在
        3、根据查找结果，进行添加还是不能操作
        4、如果不存在，则输入学生信息
        给计算机，进行添加操作
        :param computer:
        :return:
        """
        code = input('输入学生学号:')
        result = computer.searchstudent(code)
        if result is not None:
            print('学生存在，在{}组，信息如下:{}'.format(
                result[0],
                result[-1]
            ))
            return

        name = input('输入学生名称:')
        age = int(input('输入学生年龄:'))
        score = int(input('输入学生成绩:'))
        student = Student(code, name, age, score)

        keys = tuple(computer.students.keys())
        print('当前组有如下', keys)
        key = ''
        while key not in keys:
            key = input('请输入正确组名:')

        return key, student


    def te_removestudent(self):
        pass


class Computer:
    teachers = [
        Teacher('101', 'lwy'),
        Teacher('102', 'xiasisi')
    ]
    students = {'Computer': [],
                'Math': [],
                'Chinese': [],
                'Star': [],
                'Python': []}

    def __init__(self):
        self.teacher = None

    def showmenu(self):
        print('1、添加学生')
        print('2、删除学生')
        print('3、打印小组信息')
        print('4、打印所有学员信息')
        print('5、筛选学员')
        print('6、退出')
        n = int(input('请输入菜单:'))
        return n

    def addstudent(self):
        result = self.teacher.te_addstudent(self)
        if result is None:
            print('添加失败')
            return
        key = result[0]
        student = result[-1]

        self.students[key].append(student)
        print('添加成功')

    def removestudent(self):
        pass

    def showonegroupinfo(self):
        pass

    def showallinfo(self):
        print('*' * 10, '所有学生信息如下:')
        for key, stus in self.students.items():
            if len(stus) == 0:
                continue
            print('{}组信息如下:'.format(key))
            for stu in stus:
                print(stu)

        print('*' * 30)

    def filterstudents(self):
        pass

    def searchstudent(self, code):
        for key, stus in self.students.items():
            for stu in stus:
                if stu.code == code:
                    return key, stu
        print('学生不存在')

    def login(self):
        code = input('输入工号:')
        name = input('输入名字:')
        for teacher in self.teachers:
            if teacher.code == code and teacher.name == name:
                return teacher

    def start(self):
        # 登录
        teacher = self.login()
        if teacher is None:
            print('登录失败')
            return
        print('登录成功, 欢迎', teacher.name)
        self.teacher = teacher

        while True:
            n = self.showmenu()
            if n == 1:
                self.addstudent()
            elif n == 2:
                pass
            elif n == 4:
                self.showallinfo()
            elif n == 6:
                break


if __name__ == '__main__':
    computer1 = Computer()
    computer1.start()