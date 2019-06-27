import numpy as np
import csv    #需要加载numpy和csv两个包
# date_List = []
# with open(basedir, 'r') as f:#打开文件
#     csv_reader_lines = csv.reader(f)    #用csv.reader读文件
#
#     for one_line in csv_reader_lines:
#         date_List.append(one_line)    #逐行将读到的文件存入python的列表
# date_List = date_List[1:]
# data_ndarray = np.array(date_List)    #将python列表转化为ndarray
# print(data_ndarray[0:3])    #切个片试一下是否成功

beike_date_path = './data.csv'
t1 = np.loadtxt(beike_date_path, delimiter=',')
print(t1)