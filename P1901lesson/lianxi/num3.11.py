#  求100以内的素数

i = 2
for i in range(2, 101):
   j = 2
   for j in range(2, i):
      if(i % j == 0):
         break
   else:
    print(i)




# 编写一个函数，输入n为偶数时，调用函数求1/2 + 1/4 + ... + 1/n；
# 当输入n为奇数时，调用函数求1/1 + 1/3 + ... + 1/n
def cal(n):
   for i in range(abs(n % 2 - 2), n + 1, 2):
      print('{}/{}'.format(1, i))

cal(9)