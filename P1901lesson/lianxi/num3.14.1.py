# 请仔细阅读以下场景
# 某学校，要制作一次班级学生excel表格进行一次学生比赛信息录入，班级学生以小组形式进行比赛,
# 每位选手根据自己的发言，可得到一定的分数，
# 表格中包涵，小组名、学号(唯一)、姓名、年龄、比赛个人成绩等基本信息，
# 学生小组名单为固定列表中选择: Computer、Math、Chinese、Star、Python
# 1）可手动添加一名学生，放入某个小组下；
# 2）可手动删除一名学生，从表格中移除；
# 3）可打印整个小组学生信息,按学号进行排序；
# 4）显示整个班级所有小组总成绩及小组成员平均成绩；
# 5）可筛选整个班级所有学生在某两个分数成绩之间的所有信息，或者根据年龄进行筛选；

# class Student:
#     def __init__(self, team, code, name, age, score):
#         self.team = team
#         self.code = code
#         self.name = name
#         self.age = age
#         self.score = score
#     def __str__(self):
#         return '小组:{}, 学号:{}, 姓名:{}, 年龄:{}, 成绩:{}'.\
#             format(self.team, self.code, self.name, self.age, self.score)
#
#
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#
#     def showinput(self):
#         return  int(input('请选择菜单:'))
#
#     def t_addstudent(self, computer):
#         code = input('输入学生学号:')
#         student = computer.findstudent(code)
#         if student is not None:
#             print('该学生已经存在{}'.format(student))
#         else:
#             team = input('请输入小组:')
#             code = input('请输入学生学号:')
#             name = input('请输入姓名:')
#             age = int(input('请输入年龄:'))
#             score = input('请输入成绩:')
#             newstudent = Student(team, code, name, age, score)
#             return newstudent, team
#
#
#
#
#     def t_deletestudent(self):
#         pass
#
#
# class Computer:
#     students = {'computer': [], 'math': [], 'chinese': [], 'star': [], 'python': []}
#     def __init__(self):
#         self.teachers = None
#
#     def shown(self):
#         print('1 添加一名学生，放在某一个小组')
#         print('2 从表格中删除某一位学生')
#         print('3 打印小组信息，按学号排序')
#         print('4 显示整个班级所有小组总成绩及小组成员平均成绩')
#         print('5 筛选出班级学生在某个分数段之间的所有信息')
#         n = self.teachers.showinput()
#         return n
#
#     def findstudent(self, code):
#         keys = self.students.keys()
#         for student in keys:
#             for stu in self.students[student]:
#                 if stu.code == code:
#                     return stu
#
#                 print('没找到该学生')
#
#     def addstudent(self):
#         result = self.teachers.t_addstudent(self)
#         if isinstance(result[0], Student):
#             team = result[-1]
#             self.students[team].append(result[0])
#             print('学生添加成功')
#
#
#
#
#
#
#
#     def start(self, teachers):
#         self.teachers = teachers
#         while True:
#             n = self.shown()
#             if n == 1:
#                 self.addstudent()
#             if n == 2:
#                 pass
#             if n == 3:
#                 pass
#             if n == 4:
#                 pass
#             if n == 5:
#                 pass
#             if n == 6:
#                 break
#
# if __name__ == "__main__":
#     teacher = Teacher('李老师')
#     computer = Computer()
#     computer.start(teacher)



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

    def te_removestudent(self, computer):
        code = input('输入要删除的学生编号：')
        result = computer.searchstudent(code)
        if result is not None:
            return result

    def te_filter(self, computer):
        start = int(input('请输入最低成绩：'))
        end = int(input('请输入最高成绩：'))
        return start, end


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
        print('5、筛选指定成绩区间的所有学员')
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
        result = self.teacher.te_removestudent(self)
        if result is not None:
            key = result[0]
            stu = result[-1]
            self.students[key].remove(stu)
            print('删除成功')

    def filter(self):
        result = self.teacher.te_filter(self)
        dict1 = {}
        for key, stus in self.students.items():
            for stu in stus:
                if result[0] <= stu.score <= result[-1]:
                    dict1[stu.name] = stu.score
        print('*' * 10, '该区间的学生和分数如下：')
        print(dict1)

    def showonegroupinfo(self):
        keys = tuple(self.students.keys())
        print('当前组有如下', keys)
        key = ''
        while key not in keys:
            key = input('请输入正确组名:')
        print('*' * 10, '{}小组的信息如下：'.format(key))
        for stu in self.students[key]:
            print(stu)

    def showallinfo(self):
        print('*' * 10, '所有学生信息如下:')
        for key, stus in self.students.items():
            if len(stus) == 0:
                continue
            print('{}组信息如下:'.format(key))
            for stu in stus:
                print(stu)

        print('*' * 30)



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
                self.removestudent()
            elif n == 3:
                self.showonegroupinfo()
            elif n == 4:
                self.showallinfo()
            elif n == 5:
                self.filter()
            elif n == 6:
                break


if __name__ == '__main__':
    computer1 = Computer()
    computer1.start()
