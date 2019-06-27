"""
# 根据以下场景，模拟一个自助购物系统：
# 场景：市场上有一家新店开业，为了吸引顾客光临，现将部分商品出售，派克钢笔（单价200）、茶杯(单价50)、毛巾(单价20)、
书(单价20)、拖鞋(单价10)等商品，每位顾客进店，可手持一个购物车进行选购商品，选购完成后，总价在500元以上时，商家会优
惠50元，1000元优惠100元，依次累加优惠政策，结账时可直接抵现；
# 功能细则如下：
# 1）可查看目前商品信息（商品名及单价）；
# 2）查看当前购物车中商品信息：需要显示当前商品名称、商品单价、当前购物车商品数量等相关信息，以及购物车中商品总价；
# 3）添加商品到购物车：可根据商品名称，放入购物车中（默认添加一件）；
# 4）减少移出购物车中的指定商品；
# 5）结账，离开购物车系统，显示最终价格及购买的商品列表明细；

"""







def showallinfo(goods):
    """
    显示所有商品信息
    """
    print('所有商品信息如下:')
    for good in goods:
        print('名称:{}, 单价:{}'.format(good['name'], good['price']))
    print('*' * 30)

def showshopingcarinfo(goods):
    """
    显示购物车信息
    """
    print('*' * 10, '购物车信息如下:')
    s = 0
    for good in goods:
        if good['number'] > 0:
            s = s + good['price'] * good['number']
            print('名称:{}, 单价:{}, 数量:{}, 该商品总价:{}'
                  .format(good['name'], good['price'], good['number'],
                          good['price'] * good['number']))
    if s == 0:
        print('购物车是空的')
    else:
        print('购物车目前总价:', s)
    return s


def addgood(goods):
    """
    添加商品到购物车
    1、输入商品名称，判定商品是否存在
    2、如果存在，则默认将数量+1
    3、如果不存在，则不能操作
    """
    showallinfo(goods)
    name = input('输入商品名称:')
    good = searchgood(name, goods)
    if good is not None:
        good['number'] += 1
        print('添加成功')
    else:
        print('商品不存在，不能执行添加操作')

def removegood(goods):
    """
    从购物车中移除商品
    1、显示购物车信息
    2、输入商品名称，判定商品是否存在
    3、如果商品存在，判定数量是否>0,
    4、都符合标准，则默认数量-1
    5、否则，不能操作
    """
    showshopingcarinfo(goods)
    name = input('输入商品名称:')
    good = searchgood(name, goods)
    if good is not None and good['number'] > 0:
        good['number'] -= 1
        print('移除成功,当前商品剩余:', good['numebr'])
    else:
        print('商品不在购物车或者不在列表中,不能操作')

def searchgood(name, goods):
    """
    查询商品是否存在
    """
    for good in goods:
        if name == good['name']:
            return good

def showmenu():
    print('1、显示商品信息')
    print('2、添加商品到购物车')
    print('3、移除商品出购物车')
    print('4、查看购物车')
    print('5、结账退出')
    n = int(input('请选择菜单:'))
    return n


if __name__ == '__main__':
    goodslist = [
        {'name': 'pen', 'price': 200, 'number': 0},
        {'name': 'cup', 'price': 50, 'number': 0},
        {'name': 'book', 'price': 20, 'number': 0}
    ]
    while True:
        n = showmenu()
        if n == 1:
            showallinfo(goodslist)
        elif n == 2:
            addgood(goodslist)
        elif n == 3:
            removegood(goodslist)
        elif n == 4:
            showshopingcarinfo(goodslist)
        elif n == 5:
            s = showshopingcarinfo(goodslist)
            money = s // 500 * 50
            print('商品优惠{}, 需要支付{}'
                  .format(money, s - money))
            break