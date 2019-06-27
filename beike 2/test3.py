from matplotlib import pyplot as plt
from matplotlib import font_manager

#myfont让图标显示中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y1 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)

# 图片大小
plt.figure(figsize=(20, 8), dpi=80)
# lable 图例内容 color 图像颜色 linestyle 虚线 linewidth 线条粗细
plt.plot(x, y, label='自己', color='orange', linestyle=':')
plt.plot(x, y1, label='同桌', color='cyan')

# 设置x刻度
_xtick_lables = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_lables, FontProperties=my_font)
plt.savefig('./t3.png')

# 绘制网格
plt.grid(alpha=0.4)

# 添加图例， prop：显示中文
plt.legend(prop=my_font)

# 打印
plt.show()

