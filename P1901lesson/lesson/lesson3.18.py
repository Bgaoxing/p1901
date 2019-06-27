# 冒泡排序

# l = [44, 11, 66, 22, 55, 33]
#
# i = 0
# while i < len(l) - 1:
#     j = 0
#     while j < len(l) - i - 1:
#         if l[j] > l[j + 1]:
#             temp = l[j]
#             l[j] = l[j + 1]
#             l[j + 1] = temp
#             # l[j], l[j + 1] = l[j + 1], l[j]
#
#         j += 1
#     i += 1
# print(l)



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' ' + str(self.age)


s1 = Student('zhangsan', 10)
s2 = Student('lisi', 10)
s3 = Student('wanglaowu', 20)
s4 = Student('lisi', 5)

l = [s1, s2, s3, s4]

# newl = sorted(l, key=lambda x:x.name)
newl = sorted(l, key=lambda x:(x.name, x.age))

for stu in newl:
    print(stu)