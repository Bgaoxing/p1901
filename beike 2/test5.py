from pyecharts import Bar
import pymongo
# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()

# bar = Bar('成都市各区新房均价图', '主要区')
# bar.add('房价', ['成华区', '武侯区', '锦江区', '青羊区'], [25000, 18000, 15000, 14000])
# bar.render()
from pymongo import MongoClient
def get_db(): # 库
    client = MongoClient(maxPoolsize=None, connect=False)
    db = client.runoob  ##changle_research_data
    return db
def query_db(db): # 集合
    data = db['test']
    address = {}
    for d in data:
        if d['district'] not in address:
            address[d['district']] = 1
        else:
            address[d['district']] += 1
    attr = [i for i in address]



