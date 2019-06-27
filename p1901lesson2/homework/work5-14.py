# class MyList:
#     def __init__(self, iterable=()):
#         self.data = list(iterable)
#
#     def __repr__(self):
#         return 'MyList({})'.format(self.data)
#
#     def __add__(self, rhs):
#         return MyList(self.data + rhs.data)
#
#
#
# L1 = MyList([1, 2, 3])
# L2 = MyList([4, 5, 6])
#
# L3 = L1 + L2
# print(L3)
#



class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList({})'.format(self.data)

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __iadd__(self, rhs):
        self.data += rhs.data
        return self


L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])

L2 += L1  # 调用 __iadd__方法
print(L2)
