# 上课代码
# import 路径
# 问： import和include 区别  "" <>
# import 避免重复


import jxh.jxhfunc

# print(jxh.jxhfunc.num())
jxh.jxhfunc.num(78, 98, 45, 12, 9, 100)

# 第二种
# from 大路径名 import  小路径名
# from  jxh import  jxhfunc
# jxhfunc.num()
#
# 精确引入： （缺点：智能是要部分引入）
# from  jxh.jxhfunc import  num
#
# 全部引入：（缺点：容易造成重名）不推荐
# from  jxh.jxhfunc import *


def num():
    print('1111')

num()

# import  math as m
# print(m.pi)