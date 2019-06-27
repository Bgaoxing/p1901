import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
from matplotlib import font_manager

#myfont让图标显示中文字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
#实例化客户端
client = MongoClient(host='127.0.0.1', port=27017)
#绑定数据库
db = client.runoob
#绑定数据集合
collection = db['test']

#不同区域的小区总数并按区域分组的查找代码
pipeline= [{"$group": {"_id": '$district', "count": {'$sum': 1}}}]

#plt.figure定义图表大小
plt.figure(figsize=(20, 8), dpi=80)

#使用聚合查询
m = collection.aggregate(pipeline)
x = []
y = []
#查出来的数据标示不同轴
for i in m:
    x.append(i['_id'])
    y.append(i['count'])
print(x)
print(y)
#绘图
plt.scatter(x, y)#点状图
plt.plot(x, y)#线状图
for a, b in zip(x, y):#给每个点标上一个值
    plt.text(a, b+2, '%.0f'%b, ha='center', va='bottom', fontsize=12)

#让x轴显示中文并倾斜45度
plt.xticks(rotation=45, fontproperties=my_font)

plt.xlabel('地区', fontproperties=my_font, fontsize=14)#给不同轴命名
plt.ylabel('房源数',fontproperties=my_font, fontsize=14)
plt.title('成都各区域房源数', fontproperties=my_font, fontsize=14)#给图标命名

plt.savefig('./t1.png')  # 保存（本地）
plt.show()