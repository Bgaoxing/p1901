# 循环
# break  终止本层循环 不管该层循环break后还剩多少语句或次数  都不再执行
# continue  终止本次循环 该次之后的语句不再执行，但继续下次执行

# t中是否有11
# t = (11, 22, 33, 44, 55, 66, 77, 88)
#
# i = 0
# while i < len(t):
#     if t[i] == 11:
#         print('找到了')
#     break
    #continue
# print(i)

# 银行登陆 提示输入密码 （3次机会）
# 密码正确 登陆成功
# 登陆失败

# i = 1
# while i < 3:
#     password = (input('输入密码第{}次密码'.format(i)))
#     if password == '123456':
#         print('登录成功')
#         break
#         i = i + 1
#     if i == 3:
#         print('登陆失败')
# print('over')
#
# i = 1
# while i < 3:
#     password = (input('输入密码第{}次密码'.format(i)))
#     if password == '123456':
#         print('登录成功')
#         break
#         i = i + 1
# else:
#     print('登陆失败')
# print('over')



# while-else 判定循环是否正常结束
# t中是否有12
# t = (11, 22, 33, 44, 55, 66, 77, 88)
#
# i = 0
# while i < len(t):
#     if t[i] == 12:
#         print('找到了')
#     break
#     #continue
#     i = i + 1
# else:
#     print('找不到')
# print('over')


# for - in 遍历
for i in 'hello':
    print(i)

t = (11, 22, 33)
for i in t:
    print(t)

t = (11, 22, 33, 44, 55, 66, 77, 88)
for v in t:
    if v == 11:
        print('找到了')
        break
else:
    print('没找到')

    t = (11, 22, 33)
# range() 范围
# range(stop) 默认从0开始
# range(start, stop [, step])  step 默认为1
# for i in range(0, 100, 2):
#     print(i)


for i in range(0, 100):
    print(i)

for i in range(0, 100, 2):
    print(i)

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)
