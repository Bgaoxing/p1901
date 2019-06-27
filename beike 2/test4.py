from matplotlib import pyplot as plt
from matplotlib import font_manager

#myfont让图标显示中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

y_3 = [11,17,16,12,11,11,12,6,6,7,8,9,12,15,14,17,20,14,15,15,15,19,21,22,22,23,24,25,26,28,24]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,11,12,11]

x_3 = range(1, 32)
x_10 = range(51, 82)


# 设置图形大小
plt.figure(figsize=(20,10), dpi=80)
plt.scatter(x_3, y_3, label='3月')
plt.scatter(x_10, y_10, label='10月')

# 调整x刻度
_x = list(x_3)+list(x_10)
_xtick_lables = ['3月{}日'.format(i) for i in x_3]
_xtick_lables += ['10月{}日'.format(i - 50) for i in x_10]
# 每三天画一个点
plt.xticks(_x[::3], _xtick_lables[::3], FontProperties=my_font, rotation=45)

# 添加图例， prop：显示中文
plt.legend(prop=my_font)

# 添加描述信息
plt.xlabel('时间', FontProperties=my_font)
plt.ylabel('温度', FontProperties=my_font)
plt.title('成都市3月和10月温度散点图', FontProperties=my_font)

plt.savefig('./t4.png')
plt.show()