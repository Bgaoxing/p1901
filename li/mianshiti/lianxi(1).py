# 1、一行代码实现1—100之和
a = sum(range(0, 101))
print(a)

# 2、如何在一个函数内部修改全局变量
a = 3
def func():
    global a
    a = 4
print(a)

# 3、列出5个python标准库
# math, sys, os, datetime, random, re

# 4、字典如何删除键和合并两个字典
dic = {'name': 'zs', 'age': 18}
del dic['name']
dic1 = {'name': 'ls'}
dic.update(dic1)
print(dic)

# 5、谈下python的GIL
# GIL是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占
# python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。
# 如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先
# 后顺序的，并不是同时进行。多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
# 所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

# 6、python实现列表去重的方法
list = [1, 1, 2, 3, 4, 4]
a = set(list)
print([i for i in a])

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
# 不定参数与关键字参数：*args 不知道要传多少个参数时使用，*kwargs 就是当你传入key=value是存储的字典, 如下例：
def test(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
test(1,2,3,d='4',e=5)

# 8、python2和python3的range（100）的区别
# python2 返回列表 python3 返回迭代器，节约内存

# 9、一句话解释什么样的语言能够用装饰器?
# 函数能够当参数传递的语言

# 10、python内建数据类型有哪些
# int str tuple list bool dict

# 11、简述面向对象中__new__和__init__区别
# __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
# 1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
# 2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名,cls)）__new__出来的实例，或者直接是object的__new__出来的实例
# 3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，
# 那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

# 12、简述with方法打开处理文件帮我我们做了什么？
# 打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，
# 都要执行finallyf.close()关闭文件，with方法帮我们实现了finally中f.close

# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list = [1, 2, 3, 4, 5]
def fun(x):
    return x**2
res = map(fun, list)
res1 = [i for i in res if i > 10]
print(res1)

# 14、python中生成随机整数、随机小数、0—1之间小数方法
import random
import numpy as np
a = random.randint(10, 20) # 区间内整数
b = np.random.randn(5) # 随机生成5个小数
c = random.random() # 0-1 随机小数
print(a)
print(b)
print(c)

# 15、避免转义给字符串加哪个字母表示原始字符串？
# r,表示需要原始字符串，不转义特殊字符

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
import re
str = '<div class="name">中国</div>'
# .代表可有可无 *代表任意字符 满足类名可以变化 （.*?）提取文本
res = re.findall(r'<div class=".*">(.*?)</div', str)
print(res)

# 17、python中断言方法举例
# assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错
a = 3
assert (a > 2)
print('断言成功，继续执行')
# b = 4
# assert (a > 5)
# print('断言失败，报错')

# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
#select distinct name from student

# 19、10个Linux常用命令
#ls查看所有目录 pwd查看当前路径 cd切换目录 rm删除文件或目录 mkdir创建目录 cp复制  find搜索目录或文件
#tar解压 date显示日期 mv移动文件或者将文件改名 echo输出命令：'echo [选项] [输出内容]'

# 20、python2和python3区别？列举5个
#1、Python3使用print必须要以小括号包裹打印内容，比如print('hi')Python2既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如print'hi'
# 2、python2range(1,10)返回列表，python3中返回迭代器，节约内存
# 3、python2中使用ascii编码，python中使用utf‑8编码
# 4、python2中unicode表示字符串序列，str表示字节序列python3中str表示字符串序列，byte表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要6、python2中是raw_input()函数，python3中是input()函数

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 可变：list dict
# 允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
# 不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。
# 不可变 tuple string 数值型
# 不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址）

# 22、s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
# 使用sort()方法对list排序会修改list本身,不会返回新list，通常此方法不如sorted()方便，
# 但是如果你不需要保留原来的list，此方法将更有效sort()。sort()不能对dict字典进行排序
s = 'ajldjlajfdljfddd'
a = set(s)
b = [i for i in a]
b.sort(reverse=False)
print(b)

# 23、用lambda函数实现两个数相乘
a = lambda x, y: x * y
a(2, 3)

# 24、字典根据键从小到大排序dict={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”}
dict = {'name': 'zs', 'age': 18, 'city': '深圳', 'tel': '1362626627'}
dict1 = sorted(dict.items(), key=lambda x: x[0])
print(dict1)

# 25、利用collections库的Counter方法统计字符串每个单词出现的次数”kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h”
from collections import Counter
s = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
a = Counter(s)
print(a)

# 26、字符串a = “not 404 found 张三 99 深圳”，每个词中间是空格，用正则过滤掉英文和数字，最终输出”张三  深圳”
import re
a = 'not 404 found 张三 99.5 深圳'
list = a.split(' ')
# d+表示数字 .?小数 d*尽可能多的匹配数字
res = re.findall('\d+\.?\d*|[a-zA-Z]+', a)
for i in res:
    if i in list:
        list.remove(i)
new_str = ' '.join(list)
print(new_str)

# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] filter 用于筛选
# %求余 //取整除 商的整数部分
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
    return a % 2 == 1
list = filter(fn, a)
print([i for i in list])

# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i % 2 == 1]
print(res)

# 29、正则re.complie作用
# complie 生成正则表达式对象（正则本来需要做复杂的运算，complie帮助运算）

# 30、a=（1，）b=(1)，c=(“1”) 分别是什么类型的数据？
a = (1,)
b = (1)
c = ('1')
print(type(a))
print(type(b))
print(type(c))

# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
a = [1, 5, 7, 9]
b = [2, 2, 6, 8]
a.extend(b)
a.sort(reverse=False)
print(a)

# 32、用python删除文件和用linux命令删除文件方法
# python: os.remove(文件名)
# linux: rm 文件名

# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
#import datetime
# a = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期:' + str(datetime.datetime.now().isoweekday())

# 34、数据库优化查询方法
# 外键 索引 联合查询 选择特定字段等

# 35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
# matplotlib, pychart

# 36、写一段自定义异常代码
def fun():
    try:
        for o in range(5):
            if i > 2:
                raise Exception('数字大于2了')
    except Exception as ret:
        print(ret)
fun()

# 37、正则表达式匹配中，（.*）和（.*?）匹配区别？
# （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
# （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
s = '<a>哈哈</a><a>呵呵</a>'
import re
res = re.findall('<a>(.*)</a>', s)
print('贪婪匹配', res)
res1 = re.findall('<a>(.*?)</a>', s)
print('非贪婪匹配', res1)

# 38、简述Django的orm
# ORM，全拼Object-Relation Mapping，意为对象-关系映射
# 实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码只需要面向对象编程,
# orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层
# 使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可

# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1, 2], [3, 4], [5, 6]]
x = [j for i in a for j in i]
print(x)
# 将列表转成numpy矩阵，通过numpy的flatten（）方法
import numpy as np
b = np.array(a).flatten().tolist()
print(b)

# 40、x=”abc”,y=”def”,z=[“d”,”e”,”f”],分别求出x.join(y)和x.join(z)返回的结果
x = 'abc'
y = 'def'
z = ['d', 'e', 'f']
m = x.join(y)
n = x.join(z)
print(m)
print(n)

# 41、举例说明异常模块中try except else finally的相关意义
# try except else 没有捕获到异常，执行else语句
# try except finally 不管是否捕获到异常，都执行finally语句

# 42、python中交换两个数值
a, b = 3, 4
a, b = b, a
print(a, b)
# 43、举例说明zip（）函数用法
# zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。
# 同时将这些序列中并排的元素配对。
# zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，
# zip能自动以最短序列长度为准进行截取，获得元组。
a = [1, 2]
b = [3, 4]
print([i for i in zip(a, b)])
a = (1, 2)
b = (3, 4)
print([i for i in zip(a, b)])
a = 'ab'
b = 'qwe'
print([i for i in zip(a, b)])

# 44、a=”张明 98分”，用re.sub，将98替换为100
# sub是substitute的所写，表示替换
a = '张明 98分'
ret = re.sub(r'\d+', '100', a)
print(ret)
# 45、写5条常用sql语句
# select * from   show   update set   create  order by

# 46、a=”hello”和b=”你好”编码成bytes类型
a = b'hello'
b = '你好'.encode()
print(type(a), type(b))

# 47、[1,2,3]+[4,5,6]的结果是多少？
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
# 48、提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存
# 2、循环代码优化，避免过多重复代码的执行
# 3、核心模块用Cython  PyPy等，提高效率
# 4、多进程、多线程、协程
# 5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

# 49、简述mysql和redis区别
# redis：内存型非关系数据库，数据保存在内存中，速度快（hash表，查找快，但不能做复杂的搜索）
# mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的IO操作，访问速度相对慢(数据存在树形结构中，可以做复杂的搜索)

# 50、遇到bug如何处理
#1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
#2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
#3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会
# 一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
#4、导包问题、城市定位多音字造成的显示错误问题

# 51、1、正则匹配，匹配日期2018-03-20
# ^在正则表达式中有两个作用，一是表达以什么开头: 当st = r'abc'时,字符串中有'abc'就匹配成功,当st = r'[abc]'时,字符串中只要有'a'或'b'或'c'，就匹配出来
# 当st = r'^abc'时,字符串中只有'abc'开头的才匹配出来, 后同
# 二是表达对什么取反：'[^a-z]' 所有小写字母之外的字符， '[^a-zA-Z]' 所有大写和小写字母之外的字符， '[^0-9]' 所有数字之外的字符
# url=’https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462‘

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
a = re.findall(r'dateRange=(.*?)%7C(.*?)&', url)
print(a)
# 52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
l1 = [2, 3, 5, 4, 9, 6]
l2 = []
while len(l1) > 0:
    m = min(l1)
    l1.remove(m)
    l2.append(m)
print(l2)
# 53、写一个单列模式
#
# 54、保留两位小数
# 题目本身只有a=”%.03f”%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）
#
# 55、求三个方法打印结果
#
# 56、列出常见的状态码和意义
#
# 57、分别从前端、后端、数据库阐述web项目的性能优化
#
# 58、使用pop和del删除字典中的”name”字段，dic={“name”:”zs”,”age”:18}
#
# 59、列出常见MYSQL数据存储引擎
# ”,4),(“e”,5)]
#
# 61、简述同源策略
#
# 62、简述cookie和session的区别
#
# 63、简述多线程、多进程
# 进程是资源的分配和调度的一个独立单元，而线程是CPU调度的基本单元
# 同一个进程中可以包括多个线程，并且线程共享整个进程的资源（寄存器、堆栈、上下文），一个进程至少包括一个线程。
# 线程是轻两级的进程，它的创建和销毁所需要的时间比进程小很多，所有操作系统中的执行功能都是创建线程去完成的
# 线程中执行时一般都要进行同步和互斥，因为他们共享同一进程的所有资源
# 64、简述any()和all()方法
#
# 65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
#
# 66、python中copy和deepcopy区别
#
# 67、列出几种魔法方法并简要介绍用途
#
# 68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
#
# 69、请将[i for i in range(3)]改成生成器
#
# 70、a = “  hehheh  “,去除收尾空格
#
# 71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
#
# 72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
#
# 73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
# [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
#
# 74、列表嵌套字典的排序，分别根据年龄和姓名排序
#
# 75、列表嵌套元组，分别按字母和数字排序
#
# 76、列表嵌套列表排序，年龄数字相同怎么办？
#
# 77、根据键对字典排序（方法一，zip函数）
#
# 78、根据键对字典排序（方法二,不用zip)
#
# 79、列表推导式、字典推导式、生成器
#
# 80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
#
# 81、举例说明SQL注入和解决办法
#
# 82、s=”info:xiaoZhang 33 shandong”,用正则切分字符串输出[‘info’, ‘xiaoZhang’, ‘33’, ‘shandong’]
#
# 83、正则匹配以163.com结尾的邮箱
#
# 84、递归求和
#
# 85、python字典和json字符串相互转化方法
#
# 86、MyISAM 与 InnoDB 区别：
#
# 87、统计字符串中某字符出现次数
#
# 88、字符串转化大小写
#
# 89、用两种方法去空格
#
# 90、正则匹配不是以4和7结尾的手机号
#
# 91、简述python引用计数机制
#
# 92、int(“1.4”),int(1.4)输出结果？
#
# 93、列举3条以上PEP8编码规范
#
# 94、正则表达式匹配第一个URL
#
# 95、正则匹配中文
#
# 96、简述乐观锁和悲观锁
#
# 97、r、r+、rb、rb+文件打开模式区别
#
# 98、Linux命令重定向 > 和 >>
#
# 99、正则表达式匹配出 <html><h1>www.itcast.cn</h1></html>
#
# 100、python传参数是传值还是传址？
# 101、求两个列表的交集、差集、并集
#
# 102、生成0-100的随机数
#
# 103、lambda匿名函数好处
#
# 104、常见的网络传输协议
#
# 105、单引号、双引号、三引号用法
#
# 106、python垃圾回收机制
#
# 107、HTTP请求中get和post区别
#
# 108、python中读取Excel文件的方法
#
# 109、简述多线程、多进程
#
# 110、python正则中search和match

# 冒泡排序
# 外层循环为循环的轮数，内层循环为每一轮循环的次数
l = [44, 11, 66, 22, 55, 33]
i = 0
while i < len(l) - 1:
    j = 0
    while j < len(l) - i - 1:
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
        j += 1
    i += 1
print(l)

# # 二分查找
# def fun(l, x, low, end):
#     while 1:
#         if low < end:
#             mid = (low + end) // 2
#             if x < l[mid]:
#                 end = mid - 1
#             elif x > l[mid]:
#                 low = mid + 1
#             else:
#                 return print('{}索引为{}'.format(x, mid))
#         else:
#             return print('不存在')
# l = [1, 2, 4, 5, 7, 8, 9]
# x = int(input('输入要查找的数:'))
# low = 0
# end = len(l) - 1
# fun(l, x, low, end)

# 递归  一共10000元，每天用一半，多少天用完
# 递归     求和
money = 10000
day = 0
def cost(money, day):
    if money == 0:
        print('{}天用完'.format(day))
    else:
        money = money // 2
        day += 1
        return cost(money, day)
cost(money, day)


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

res = sum(10)
print("res=", res)