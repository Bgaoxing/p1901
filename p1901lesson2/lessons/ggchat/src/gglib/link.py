class Node:
    def __init__(self):
        """
        data 存放数据
        next 指向下一个
        prev 指向上一个
        """
        self.data = None
        self.next = None
        self.prev = None

    # def __str__(self):
    #     return '{}'.format(self.data)


class Link:
    def __init__(self, data=()):
        # 初始化时首尾指向同一个值
        self.head = Node()
        self.tail = self.head
        self.data = data

        self.length = 0

        for d in data:  # 不传入时默认为空
            self.append(d)

    def __str__(self):
        return str([i for i in self])


    def __find_node_by(self, pos):
        """
        从数据头端开始查找节点
        :param pos: 传入需要查找的数据节点
        :return: 返回查找到的节点指向
        """
        nodeptr = self.head # 若pos为0，直接返回nodeptr，即第一个元素
        while pos:
            nodeptr = nodeptr.next
            pos -= 1
        return nodeptr

    def append(self, data):
        """
        在数据末尾添加数据
        :param data: 传入添加的数据
        """
        node = Node()  # 实例化数据
        node.data = data  # 添加数据
        self.tail.next = node  # 原数据的尾端指向这个数据
        node.prev = self.tail  # 原数据尾端变成新数据的上一个数据
        self.tail = node  # 数据尾端指向新数据
        self.length += 1  # 数据长度加一

    def pop(self, i=-1):
        """
        删除末尾的元素，并将这个元素返回
        :param i: 指向最后一个元素
        :return: 返回删除的元素
        """
        if len(self) <= 0:
            raise Exception("The list is empty")  # 数据为空时，抛出异常

        if i == -1:  # -1是默认，代表删除的是末尾的值
            node = self.tail  # 取到数据结构的尾端指针（即尾端的node）
            self.tail = node.prev  # 将该node数据中指向的上一个数据作为尾端指针（删除末尾值）
            self.tail.next = None  # 设置此刻尾端指针的下一个指针指向为空
            self.length -= 1
            return node.data  # 返回删除数据的值
        else:  # 指定要删除元素的下标
            node = self.__find_node_by(i)  # 根据下标查找到该元素
            cur_node = node.next  # 找到该元素的下一个值
            third_node = node.next.next  # 找到该元素的下一个的下一个值
            if third_node is not None:
                third_node.prev = node  # 如果不为空，删除找到的该元素的下一个值（直接将第三个元素的前一个值的指向改成查找到的值）
            node.next = third_node  # 如果为空，那就把找到的第二个删除即可
            self.length -= 1
            return cur_node.data  # 返回删除的元素

    def insert(self, i, data):
        """
        插入元素
        :param i:插入的值所在的位置，插入后为新值的前一个值
        :param data: 新数据的数值
        :return: None
        """
        assert i <= len(self) - 1  # 给定的下标是否超出数据的长度
        nodeptr = self.head
        while i:
            nodeptr = nodeptr.next  # 找到下标对应的值
            i -= 1

        third_node = nodeptr.next  # 得到查找到的这个值的下一个值，并打算在他们之间插入新值
        node = Node()
        node.data = data
        # 使用指向的方式在他们之间插入新值
        node.next = third_node  # 新值下一个值指向third_node
        third_node.prev = node  # third_node的上一个值指向node

        nodeptr.next = node  # nodeptr的下一个值指向node
        node.prev = nodeptr  # node的上一个值指向nodeptr
        self.length += 1  # 长度加一

    def remove(self, i):
        """
        删除i下标对应元素的下一个元素
        :param i: 查找的下标
        :return: None
        """
        assert i <= len(self) - 1
        nodeptr = self.__find_node_by(i)

        third_node = nodeptr.next.next
        nodeptr.next = third_node  # 之间删除两者之间的元素
        third_node.prev = nodeptr  # third_node的前一个指向改为nodeptr
        self.length -= 1

    def __len__(self):
        return self.length

    def __iter__(self):
        return LinkIterator(self)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, item):
        assert item <= len(self) - 1
        nodeptr = self.head.next
        while item:
            nodeptr = nodeptr.next
            item -= 1

        return nodeptr.data

    def __contains__(self, item):
        for d in self:
            if d == item:
                return True
        return False

    def __add__(self, link):
        """
        加法实现
        :param link: 加号右边的对象
        :return: None
        """
        try:
            left_node_end = self.tail
            right_node_first = link.head.next
            left_node_end.next = right_node_first
            right_node_first.prev = left_node_end
        except TypeError:
            return NotImplemented

        return self

    def __radd__(self, link):
        return self + link

    def __iadd__(self, link):
        try:
            self + link
        except TypeError:
            return NotImplemented

        return self


class LinkIterator:  # 定义一个迭代器类
    def __init__(self, link):
        self._node_ptr = link.head

    def __next__(self):
        self._node_ptr = self._node_ptr.next
        if self._node_ptr is None:
            raise StopIteration
        data = self._node_ptr.data
        return data





list = Link
x = list((1, 2, 3))
y = list([4, 5, 6])

x += y
print(x)
# x.append(1)
# x.append(2)
# x.append(3)

# for i in x:
#     print(x)

# while x:
#     print(x.pop())


# x[0] = 1
# y = x[0]
#
# for d in x:
#     for y in x:
#         print(y)


# x.insert(1, 8)
# for d in x:
#     print(d)
#
# print("\n")
# x.remove(1)
# for d in x:
#     print(d)

# if 2 in x:
#     print("2 is in list")
#
# print("The 2th is: %d" % x[1])
