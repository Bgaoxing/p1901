# 1、依次输入几个数据，直到0作为输入的结束， 然后求出输入的这些数据的总和及平均值（0不算次数）；
# count = 0
# s = 0
# while True:
#
#     n = int(input('输入数据:').format())
#
#     if n == 0:
#         break
#     count = count + 1
#     s = s + n
# count = count if count > 0 else 1
# print('总和:{},平均数{},'.format(s, s / count))





# # 2、求1000-5000之间，各位数字之和为5的所有整数，打印输出（例如整数2003的各位数字之和为2+0+0+3，等于5）
# for i in range(1000,5001):
#     if i // 1000 + i // 100 % 10 + i // 10 % 100 + i % 10 == 5:
#         print(i)
#     i += 1



# # 3、从键盘输入两个正整数，输出这个范围内的所有偶数： 如：输入 3 和9， 输出4 6 8
# start = int(input('开始的数'))
# end = int(input('结束的数'))
# if start > end:
#     temp = start
#     start = end
#     end = temp
# for i in range(start, end):
#     if i % 2 == 0:
#         print(i)
#
# # tuple补充
# t1, t2 = 11, 22
# print(t1, t2)
#
# start = int(input('输入开始的数:'))
# end = int(input('输入结束的数:'))
#
# if start > end:
#     temp = start
#     start = end
#     end = temp
#
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i)
#





# #
# # 提升：1
# # 1、输入一个五位以内的数，求每位数字之和
# for i in range(0, 10000):
#     i = int(input('输入数字').format(i))
#     print(i // 1000 + i // 100 % 10 + i // 10 % 100 + i % 10)

# n = int(input('输入一个五位数以内的整数'))
# s = 0
# while n > 0:
#     m = n % 10   # 取得最后一位
#     s = s + m
#     n = n // 10  # 去掉最后一位
# print(s)
# # 2、题目：输入某年某月某日，判断这一天是这一年的第几天？
# year, month, day = eval(input('输入年月日，用逗号隔开:'))
# t = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# days = 0
#
# i = 0
# while i < month - 1:
#     days = days + t[i]
#     i = i + 1
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     if month > 2:
#         days = days + 1
#
# days = days + day
# print('第{}天'.format(days))


# # # 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
# # 提示：元组、循环、分支

# 打印矩形
i = 0
while i < 5:

    j = 0
    while j < 6:

        print('*',end='')
        j += 1
    i = i + 1
    print()
#
# t = ((11, 22, 33),
#      (44, 55, 66),
#      (77, 88, 99))
#
#
# for v in t:
#     for v1 in v:
#         print(v1, end=' ')
#     print()

# 双层循环执行次数
# = 外层循环次数  *  内层循环次数

# i = 0
# while i < 4:
#
#     i = i + 1
#     j = 0
#     while j < 6:
#         j = j + 1
#         print('*', end='')
#
#     print()

# i = 0
# while i < 4:
#
#     j = 0
#     while j < 6:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()

"""
*       0  1*
**      1  2*
***     2  3*
****    3  4*
*****   4  5*
******  5  6*
        i  j=i + 1
"""

# i = 0
# while i < 6:
#
#     j = 0
#     while j < i + 1:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()
"""
******   0  6*
*****    1  5*
****     2  4*
***      3  3*
**       4  2*
*        5  1*
        i   j = 6 - i
"""
# i = 0
# while i < 6:
#
#     j = 0
#     while j < 6 - i:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()

"""
******   0  空格0  *6
 *****   1     1   5
  ****   2     2   4
   ***   3     3   3
    **   4     4   2
     *   5     5   1
        i    k=i   j=6-i

"""

# i = 0
# while i < 6:
#
#     # 空格
#     k = 0
#     while k < i:
#         print(' ', end='')
#         k = k + 1
#     # * 号
#     j = 0
#     while j < 6 - i:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()

"""
     *   0  5  1
    **   1  4  2
   ***   2  3  3
  ****   3  2  4
 *****   4  1  5
******   5  0  6
"""
# i = 0
# while i < 6:
#
#     # 空格
#     k = 0
#     while k < 5 - i:
#         print(' ', end='')
#         k = k + 1
#     # * 号
#     j = 0
#     while j <1 + i:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()

"""
   A
  ABA
 ABCBA
ABCDCBA


   1
  121
 12321
1234321

"""

# 1、从键盘输入一个正整数x，打印输出从0开始的连续n个偶数，如 x = 5,输出 0 2 4 6 8
# x = int(input('输入一个正整数'))
# for i in range(x):
#         print(i % 2)

# for i in range(2 * x):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(0, 2 * x, 2):
#     print(i)



# 2、打印100-999中不能被7整除又不包含7的数
# for i in range(100, 1000):
#     if i % 7 != 0 and i // 100 != 7 and i % 100 // 10 != 7 and i % 10 != 7:
#         print(i)
#
# for i in range(100, 1000):
#     if i % 7 != 0 and '7' not in str(i):
#         print(i)





#
# 提升题：
# 1、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
# a = int(input('输入一个大于0的数'))
# n = int(input('输入多少个'))
# s = a
# string = str(a)
# for i in range(n - 1):
#     a = a * 10 + a % 10
#     s = s + a
#     string = string + '+' + str(a)
# print(string, '=', s)

# 2、题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
numerator = 2  # 分子
denominator = 1  #分母
s = numerator / denominator
for _ in range(5):
    numerator = numerator + denominator
    denominator = numerator - denominator
    print('{} / {}'.format(numerator, denominator))
    s = s + numerator / denominator
print(s)
# # 程序分析：请抓住分子与分母的变化规律。
# 李文玉-成都睿峰科技有限  17:17:03
# 经典笔试题：
# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# # 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# # 程序分析：采取逆向思维的方法，从后往前推断。
#
# 经典面试题：
'''

   1
  2 3
 4 5 6
7 8 9 0

'''
# for i in range(5, 0, -1):
#     print(i)
#
# a = 'a'
# print(a > 'b' or 'c')