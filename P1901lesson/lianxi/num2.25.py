# 基础题：
# 1、定义一个变量。用来存储我卡上有100块钱，到银行存了1000块钱，打印输出现在我卡上多少钱
a=100
print(a+1000)
# 2、班费有199块钱，买了30支笔，每支笔2.5元，买了5个杯子，5元一个，打印输出班费还剩多少钱？
a=199
print(a - 30 * 2.5 - 5 * 5)
# 3、使用运算符，求19的个位打印输出；求29的十位数字打印输出；189的每位数字输出；
print(19 % 10 , 29 // 10 , 189 // 100 , 189 // 10 % 10,189 % 10)
#
# 提高题：
# 4、已知一个学生两科成绩：语文90；英语66；求该学生总成绩和平均成绩
yuwen = 90
yingyu = 66
print(yuwen + yingyu , (yuwen + yingyu) / 2)
# 5、已知正方形边长为4，求正方形周长和面积
a = 4
print(4 * 4 , 4 ** 2)
# 6、已知一个圆半径为3.5，声明一个变量名为radius存储该圆半径，要求输出该圆的半径、周长和面积
radius = 3.5
print(radius , 3.14 * radius * 2 , 3.14 * radius ** 2)

input('你输入的内容是 ' + 'helloworld')