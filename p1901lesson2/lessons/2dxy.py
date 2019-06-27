from matplotlib import pylab
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.xlabel('some ')
# plt.show()

# 默认plot(x,y)只有一个的时候为y，x为y索引
# pylab.plot([1, 2, 3, 4, 5])
# pylab.ylabel('numbers')
# pylab.show()


# 加一

import pylab as pl

x = [100, 50, 80, 70]
y = [1, 2, 3, 4]
'''
plot参数说明：
    x:  x轴坐标列表
    y:  y轴坐标列表
    marker: 点型
    linestyle:  连接线型
    markerfacecolor:
'''
pl.plot(x, y, marker='o', linestyle='--', markerfacecolor='r')
'''
axis参数说明：[x轴最小值，x轴最大值，y轴最小值，y轴最大值]的列表
它指定了坐标轴的视点
'''
pl.axis([0, 110, 0, 6])
pl.xlabel('x_data')
pl.ylabel('y_data')
pl.title('test plot')
pl.show()

# 限制范围
# plt.plot([1, 2, 3, 4], [1, 4, 9, 21], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

import numpy as np

# evenly sampled time at 200ms intervals
# np.arange()函数
# t = np.arange(0, 5, 0.2)
#
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#
# # 储存
# plt.savefig('./gg2.png')
# plt.show()


# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# x = [0,2,4,6,8,10]
# y = [0]*len(x)
# s = [20*4**n for n in range(len(x))]
# plt.scatter(x,y,s=s)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
#
# fig=plt.figure(figsize=(8,6))
# #Generating a Gaussion dataset:
# #creating random vectors from the multivariate normal distribution
# #given mean and covariance
# mu_vec1=np.array([0,0])
# cov_mat1=np.array([[1,0],[0,1]])
# X=np.random.multivariate_normal(mu_vec1,cov_mat1,500)
# R=X**2
# R_sum=R.sum(axis=1)
# plt.scatter(X[:,0],X[:,1],color='green',marker='o',
#             s=32.*R_sum,edgecolor='black',alpha=0.5)
#
#
# plt.show()

# 为x轴
# names = ['group_a', 'group_b', 'group_c']
# # 为y轴
# values = [1, 20, 100]
# # figsize图像大小 宽度，高度英寸
# plt.figure(figsize=(10, 3))
# # 位置一行三列一号位
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()