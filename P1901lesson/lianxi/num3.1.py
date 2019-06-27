# 练习：（函数完成）
# # 1、输出1-100以内所有含6的数；所有含1的数；所有含9的数；所有含8的数
# def containnumber(number):
#     for i in range(1, 101):
#         if str(number) in str(i):
#             print(i)
#
#
# containnumber(6)


# # 2、求任意一个正整数的所有位数之和（1234 = 1 + 2 + 3 + 4 = 10）

# def num(n):
#     s = 0
#     for i in range(n):
#         m = n % 10  # 取得最后一位
#         s = s + m
#         n = n // 10  # 去掉最后一位
#     print(s)
# num(3456)



# # 3、输出任意某个范围的所有偶数
# def num(start, stop):
#     for i in range(start, stop + 1):
#         if i % 2 == 0:
#             print(i)
#         i += 1
# num(1, 100)



# # 4、提供登录用户名和密码，验证登录是否成功
# (判断真假时参数用is开头)
# def islogin(user, password):
#
#         if user == 'zs' and password == 123456:
#             print('登陆成功')
#         else:
#             print('登陆失败')
# islogin(123, 123456)



# # 5、输出任意长宽的*号矩阵
# def num(long, wide):
#     i = 0
#     while i < long:
#
#         j = 0
#         while j < wide:
#             print('*', end='')
#             j += 1
#         i = i + 1
#         print()
# num(4, 5)



# # 6、求任意一个正整数的边位置是否相同，
# # 如101返回True和1；
# # 22返回True和2；
# # 3返回False和-1；
# # 302返回False和-1；
def equalnumber(number):
    if number < 0:
        return
    if number < 10:
        return  False, -1
    string = str(number)
    if string[0] == string[-1]:
        return  True,string[0]
    return False, int(string[0])
    return  False, -1

print(equalnumber(202))



# # 7、写一个函数，求多个数的最大值
def num(t):
    print(max(t))

num(t=(78, 98, 45, 12, 9, 100))


#def mymax(x, y):
#     return x if x > y else y
#
#
# a = mymax(10, 20)
# b = mymax(a, 40)
# c = mymax(b, 100)
#
# print(mymax(mymax(mymax(10, 20), 40), 100))

# def mymax(*args):
#     print(args)
#     m = args[0]
#     for i in args:
#         if m < i:
#             m = i
#     return m
#
# print(mymax(10, 20, 40, 100))