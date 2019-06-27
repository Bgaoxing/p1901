# str (字符串)
# 字符串不能被修改

# s1 = 'hello'
# s2 = 'world'
# s3 = """hello"""
# s4 = '''world'''
#
# s1 = s1 + s2 #拼接
# # s1[0] = 1 # 错误 被修改了
#
#
# # capitalize   首字母大写,其他字母小写
# s = 'www.Baidui.com'
# s1 = s.capitalize()
# print(s1)
# print(s.upper())   # 所有字符转换为大写
# print(s.lower())   # 所有字符转换为小写
# print(s.swapcase())  # 交换转换
# print(s.title())     # 单词首字母大写



#  replace  替换
# print('*' * 22,'replace')
# s = 'www.baidui.com baidu'
# print(s.replace('baidu', 'google', 1))


#  split  切割
# s = '2000/10/10'
# # print(s.split('/', 1))
# print(s.rsplit('/', 1))  #从右到左
# l = s.rsplit('/')
#
# # 合拼
#
# print('-'.join(l))


#  查询
# s = 'www.baidui.com'
# print(s.find('baidu'))  #没找到返回-1
# print(s.rfind('baidu'))  #从右边开始
# print(s.index('baidu'))  #查下标
# print(s.startswith('https://'))  #开头
# print(s.endswith('.com'))   #结尾
# print(s.count('a'))  #查个数


#  格式
# s = 'hhh'
# print(s.rjust(20, '*'))

# strip
s = '*hhh*'
print(s.strip())   #去掉空格
print(s.lstrip('*'))   #去掉左边
print(s.rstrip('*'))   #去掉右边

# print(chr(65))
# print(ord('A'))
# print(chr(ord('A') + 32))

