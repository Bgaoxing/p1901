# 1 输入语文成绩
# 2 熟人数学成绩
# 3 输入英语成绩
# 4 显示所有成绩
# 5 结束退出
#
# 请选择菜单：1
# 请输入新增的语文成绩：100
# 当前学科语文，总成绩：100，所有成绩如下：【100】

def calscore(menu, s):
    keys = tuple(s.keys())  #取得所有科目
    key = keys[menu - 1]

    score = int(input('请输入新增的{}成绩:'.format(key)))
    s[key].append(score)
    print('当前{}成绩:{}'.format(key, scores[key]))


def showmenu():
    print('1、输入语文成绩:')
    print('2、输入数学成绩:')
    print('3、输入英语成绩:')
    print('4、显示所有成绩')
    print('5、退出')
    menu = int(input('请选择:'))
    return menu


if __name__ == '__main__':

    scores = {'语文': [], '数学': [], '英语': []}

    while True:
        n = showmenu()
        if 1 <= n <= 3:
            calscore(n, scores)
        elif n == 4:
            print(scores)
        elif n == 5:
            break















