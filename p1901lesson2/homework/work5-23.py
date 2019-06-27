"""二分查找"""

# def cha(a, x, low, end):
#     while 1:
#         if low <= end:
#             mid = (low + end) // 2
#             if x < a[mid]:
#                 end = mid - 1
#             elif x > a[mid]:
#                 low = mid + 1
#             else:
#                return print('{}在列表的索引为{}'.format(x, mid))
#         else:
#           return print('不在列表中')
#
# a = [1, 3, 5, 6, 8, 9, 11, 13, 16]
# x = int(input('输入一个整数： '))
# low = 0
# end = len(a) - 1
# m = cha(a, x, low, end)
# print(m)



"""二叉树"""


# class Node:
#     def __init__(self, date=None):
#         self.date = date
#         self.left = None
#         self.right = None
#
#
# class BTree:
#     def __init__(self, dataset):
#         self.root = self.create_node(dataset)
#
#     def create_node(self, dataset, i=0):
#         if i >= len(dataset):
#             return
#
#         node = Node()
#         node.data = dataset[i]
#
#         left_index = 2 * (i + 1)
#         right_index = left_index + 1
#
#         node.left = self.create_node(dataset, left_index - 1)
#         node.right = self.create_node(dataset, right_index - 1)
#
#         return node
#
#     def __loop(self, node, flag=0):
#         if flag < 0:
#             # 先序
#             yield node.data
#         if node.left:
#             for d in self.__loop(node.left):
#                 yield d
#         if flag == 0:
#             # 中序
#             yield node.data
#         if node.right:
#             for d in self.__loop(node.right):
#                 yield d
#         if flag > 0:
#             # 后序
#             yield node.data
#
#     def __iter__(self):
#         return self.__loop(self.root)
#
#
# #
# # class BTreeIterator:
# #     def __init__(self, root_node):
# #         self.node_ptr = root_node
# #
# #     def __next__(self):
#
# tree = BTree((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# for d in tree:
#     print(d)


"""
求和（递归）
假设有10000块钱，每天花一半，求多少天花完（递归）

递归调用：一个函数，调用了自身
递归函数：一个会调用自身的函数称为递归函数
方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
"""
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)
res = sum(5)
print(res)

money = 10000
day = 0
def cost(money, day):
    if money <= 0:
        print('钱花完了，花了{}天'.format(day))
    else:
        day += 1
        money = money // 2
        return cost(money, day)
cost(money, day)

# 斐波那契数列 递归／递推
def fib_recur(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i), end=' ')



def fib_loop(n):
  a, b = 0, 1
  for i in range(n+1):
    a, b = b, a + b
    return a

for i in range(20):
  print(fib_loop(i), end=' ')
