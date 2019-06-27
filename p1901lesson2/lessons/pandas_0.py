import pandas as pd
import numpy as np
import xlrd

"""
Python已成为数据分析和数据科学事实上的标准语言和标准平台之一。
Python在数据处理和准备方面一直做得很好，但在数据分析和建模方面就没那么好了。
数据分析师和数据科学家提供的各种程序库，
如NumPy、SciPy、Pandas和Matplotlib等。
两个科学运算当中最为重要的两个模块，
提供高性能、易于使用的数据结构和数据分析工具。
一个是 numpy,一个是 pandas。任何关于数据分析的模块都少不了它们两个。

pip install pandas

数值类型的，字符串，还有时间序列
pandas的常用数据类型
1：Serles 一维，带标签的数组
2：DataFrame 二维，Serles容器
"""
# t = pd.Series([1, 2, 31, 12, 3, 4])
# print(t)



# t = pd.Series([1, 2, 31, 12, 3, 4], index=('a','b','c','d','e','f'))
# t = pd.Series([1, 2, 31, 12, 3, 4], index=list('abcdef'))
# print(t)

#
# a = {"name": "zhangsan", "age": 18, "tel": 123456}
# t = pd.Series(a)
# print(t)
# print(t[0])
# print(t["name"])
# print(t[0:2])
# print(t[[1, 2]])
# print(t[["name", "age"]])
# print(len(t))

# a = pd.read_excel("./1.xlsx")
# print(a)


# t = pd.DataFrame(np.arange(12).reshape(3, 4))
# t = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'),columns=list('wxyz'))
# print(t)




# a = {"name": ["zhangsan","lisi","wangwu"], "age": [18,19,20], "tel": [123456,456,589]}
# a = [{"name": "zhandan", "age": 18, 'tel': 123456},
#      {"name": "lisi", "age": 13, 'tel': 456798},
#      {"name": "lisi", "age": 19, 'tel': 789465}]
# t = pd.DataFrame(a)
# print(t)





